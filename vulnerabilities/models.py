from django.db import models

from django.contrib.postgres.fields import JSONField

class Vulnerability(models.Model):
    cve_json = JSONField()
    #cve_id
    #cve_description
    #cve_references

    #cvss_stuff
    # cvssV3_vector_string
    # base_score
    # impact_score
    # exploitability_score

    # confidentiality impact
    # integrity impact
    # availability impact

    #user supplied values
    # confidentiality requirement
    # integrity requirement
    # availability requirement

    # Foreign Keys
    # application = models.ForeignKey(Application, on_delete=models.CASCADE)
    # hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    # os = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vulnerability'

    def __str__(self):
        return str(self.cve_json['id'] + ' - ' + self.cve_json['summary'])
    
    def severity_available(self):
        cve_id = self.cve_json['id']
        local_q = NISTCVE.objects.filter(cve_id=cve_id)
        if local_q:
            local_q = local_q.first()
            print(local_q)

        return True

    # def get_application_vulns(self, application):
        # """ Takes app as argument and returns JSON for CVEs related to apps """
        # # get related NIST obj of passed app
        # # app_nist_cpe = application.application
        # # query NISTCVE for matching cpe entries
        # # app_cpe = app_nist_entry.json_data['configurations']['nodes'][0]['cpe_match'][0]['cpe23Uri']
        # # app_cpe = 'cpe:2.3:a:' + str(app_nist_cpe.vendor) + ':' + app_nist_cpe.product + ':' + app_nist_cpe.version

        # # query for matching cves
        # # vuln_q = NISTCVE.objects.filter(json_data__configurations__nodes__0__cpe_match__0__cpe23Uri=str(app.application))
        # # vuln_q = NISTCVE.objects.filter(json_data__configurations__nodes__0__cpe_match__0__cpe23Uri__icontains=str(app.application))

        # cve_json = None
        # return cve_json
    # def get_hardware_vulns(self, hardware):
        # """ Takes hardware as argument and returns JSON for CVEs related to hardware """
        # cve_json = None
        # return cve_json
    # def get_os_vulns(self, os):
        # """ Takes os as argument and returns JSON for CVEs related to os """
        # cve_json = None
        # return cve_json

class VulnerableCPE(models.Model):
    cpe_json = JSONField()

    class Meta:
        db_table = 'vulnerable_cpe'

    def __str__(self):
        return str(self.cpe_json)
class NISTCVE(models.Model):
    cve_id = models.CharField(max_length=455)
    description = models.TextField(max_length=455)
    date_published = models.CharField(max_length=455)
    date_modified = models.CharField(max_length=455)

    # Foreign keys
    vulnerable_cpe = models.ManyToManyField(VulnerableCPE)

    def get_json_files(self):
        """ Downloads JSON files from NIST site and saves them to vulnerabilities/json_data/ """
        import requests
        import re

        r = requests.get('https://nvd.nist.gov/vuln/data-feeds#JSON_FEED')
        # https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-modified.json.zip
        # https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-recent.json.zip
        for filename in re.findall('nvdcve-1.0-[0-9]*\.json\.zip', r.text):
            print(filename)
            r_file = requests.get('https://nvd.nist.gov/feeds/json/cve/1.0/' + filename, stream=True)
            with open('vulnerabilities/json_data/' + filename, 'wb') as f:
                for chunk in r_file:
                    f.write(chunk)
        pass

    def import_json_data(self):
        """ Imports NIST CVE data from formatted csv file into django NIST data models """
        from os import listdir
        from os.path import isfile, join
        import zipfile
        import json

        files = [f for f in listdir('vulnerabilities/json_data/') if isfile(join('vulnerabilities/json_data/', f))]
        files.sort()
        for file in files:
            archive = zipfile.ZipFile(join('vulnerabilities/json_data/', file), 'r')
            jsonfile = archive.open(archive.namelist()[0])
            cve_dict = json.loads(jsonfile.read())
            jsonfile.close()
            # print(cve_dict['CVE_data_version'])
            # print(cve_dict['CVE_data_format'])
            # print(cve_dict['CVE_data_timestamp'])
            # print(cve_dict['CVE_data_numberOfCVEs'])
            total_cves = cve_dict['CVE_data_numberOfCVEs']
            cve_created_count = 0
            reference_created_count = 0
            cpe_created_count = 0
            impact_created_count = 0
            for cve in cve_dict['CVE_Items']:
                # print('')
                # print('')
                # print('')
                # # cve_id
                # print(cve['cve']['CVE_data_meta']['ID'])
                # # description 
                # print(cve['cve']['description']['description_data'][0]['value'])
                # print(cve['publishedDate'])
                # print(cve['lastModifiedDate'])
                cve_obj = NISTCVE.objects.create(
                    cve_id=cve['cve']['CVE_data_meta']['ID'],
                    description=cve['cve']['description']['description_data'][0]['value'],
                    date_published=cve['publishedDate'],
                    date_modified=cve['lastModifiedDate'],
                )
                cve_created_count += 1

                # print('')
                # print('REFERENCES')

                # references stuff
                for reference in cve['cve']['references']['reference_data']:
                    # print('     URL: ', reference['url'])
                    # print('     NAME: ', reference['name'])
                    # print('     SOURCE: ', reference['refsource'])
                    reference_obj = CVEReference.objects.create(
                        url=reference['url'],
                        name=reference['name'],
                        source=reference['refsource'],
                        cve=cve_obj
                    )
                    reference_created_count += 1

                # print('')
                # print('CONFIGS')

                # cpe stuff
                for node in cve['configurations']['nodes']:
                    cpe_match = node.get('cpe_match', 'NONE')
                    # is cpe_match none?
                    if cpe_match == 'NONE':
                        # print('NONE')
                        pass
                    else:
                        for cpe in node['cpe_match']:
                            cpe_obj, created = VulnerableCPE.objects.get_or_create(
                                cpe_json=cpe
                            )
                            cve_obj.vulnerable_cpe.add(cpe_obj)
                            if created:
                                # print('added cpe: ', cpe_obj)
                                cpe_created_count += 1

                # impact stuff
                # print('')
                # print('IMPACT')
                if 'baseMetricV3' in cve['impact'].keys():
                    # print('     BASEMETRICV3: ', cve['impact']['baseMetricV3'])
                    impact_obj = CVEV3Impact.objects.create(
                        # vector_string=cve['impact']['baseMetricV3']['cvssV3']['vectorString'],
                        # attack_vector=cve['impact']['baseMetricV3']['cvssV3']['attackVector'],
                        # attack_complexity=cve['impact']['baseMetricV3']['cvssV3']['attackComplexity'],
                        # privileges_required=cve['impact']['baseMetricV3']['cvssV3']['privilegesRequired'],
                        # user_interaction=cve['impact']['baseMetricV3']['cvssV3']['userInteraction'],
                        # scope=cve['impact']['baseMetricV3']['cvssV3']['scope'],
                        # confidentiality_impact=cve['impact']['baseMetricV3']['cvssV3']['confidentialityImpact'],
                        # integrity_impact=cve['impact']['baseMetricV3']['cvssV3']['integrityImpact'],
                        # availability_impact=cve['impact']['baseMetricV3']['cvssV3']['availabilityImpact'],
                        # base_score=cve['impact']['baseMetricV3']['cvssV3']['baseScore'],
                        # base_severity=cve['impact']['baseMetricV3']['cvssV3']['baseSeverity'],
                        # # the rest
                        # exploitability_score=cve['impact']['baseMetricV3']['exploitabilityScore'],
                        # impact_score=cve['impact']['baseMetricV3']['impactScore'],
                        v3_impact_json=cve['impact']['baseMetricV3'],
                        cve=cve_obj
                    )
                    impact_created_count += 1
                elif 'baseMetricV2' in cve['impact'].keys():
                    # print('     BASEMETRICV2: ', cve['impact']['baseMetricV2'])
                    impact_obj = CVEV2Impact.objects.create(
                        # vector_string=cve['impact']['baseMetricV2']['cvssV2']['vectorString'],
                        # access_vector=cve['impact']['baseMetricV2']['cvssV2']['accessVector'],
                        # access_complexity=cve['impact']['baseMetricV2']['cvssV2']['accessComplexity'],
                        # authentication=cve['impact']['baseMetricV2']['cvssV2']['authentication'],
                        # confidentiality_impact=cve['impact']['baseMetricV2']['cvssV2']['confidentialityImpact'],
                        # integrity_impact=cve['impact']['baseMetricV2']['cvssV2']['integrityImpact'],
                        # availability_impact=cve['impact']['baseMetricV2']['cvssV2']['availabilityImpact'],
                        # base_score=cve['impact']['baseMetricV2']['cvssV2']['baseScore'],
                        # # the rest
                        # severity=cve['impact']['baseMetricV2']['severity'],
                        # exploitability_score=cve['impact']['baseMetricV2']['exploitabilityScore'],
                        # impact_score=cve['impact']['baseMetricV2']['impactScore'],
                        # ac_insuf_info='',
                        # obtain_all_privilege=cve['impact']['baseMetricV2']['obtainAllPrivilege'],
                        # obtain_user_privilege=cve['impact']['baseMetricV2']['obtainUserPrivilege'],
                        # obtain_other_privilege=cve['impact']['baseMetricV2']['obtainOtherPrivilege'],
                        # user_interaction_required=cve['impact']['baseMetricV2']['userInteractionRequired'],
                        v2_impact_json=cve['impact']['baseMetricV2'],
                        cve=cve_obj
                    )
                    impact_created_count += 1
                else:
                    # print('     NONE')
                    pass
        
            print('Total vulns in file: ', total_cves)
            print('Total vulns created: ', cve_created_count)
            print('Unique refs created: ', reference_created_count)
            print('Unique cpes created: ', cpe_created_count)
            print('Total impacts created: ', impact_created_count)






    class Meta:
        db_table = 'nist_cve'

    def __str__(self):
        return self.cve_id
    
    def get_vulnerable_cpes(self):
        vuln_cpes = self.vulnerable_cpe.all()
        return vuln_cpes


















#tables to add
# references


class CVEReference(models.Model):
    url = models.CharField(max_length=455)
    name = models.CharField(max_length=455)
    source = models.CharField(max_length=455)

    # Foreign Keys
    cve = models.ForeignKey(NISTCVE, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cve_reference'

    def __str__(self):
        return self.name

class CVEV3Impact(models.Model):
    # cvssV3
    # vector_string = models.CharField(max_length=455)
    # attack_vector = models.CharField(max_length=455)
    # attack_complexity = models.CharField(max_length=455)
    # privileges_required = models.CharField(max_length=455)
    # user_interaction = models.CharField(max_length=455)
    # scope = models.CharField(max_length=455)
    # confidentiality_impact = models.CharField(max_length=455)
    # integrity_impact = models.CharField(max_length=455)
    # availability_impact = models.CharField(max_length=455)
    # base_score = models.CharField(max_length=455)
    # base_severity = models.CharField(max_length=455)
    # # the rest
    # exploitability_score = models.CharField(max_length=455)
    # impact_score = models.CharField(max_length=455)
    v3_impact_json = JSONField()

    # Foreign keys
    cve = models.ForeignKey(NISTCVE, on_delete=models.CASCADE)
    class Meta:
        db_table = 'cvev3_impact'

    def __str__(self):
        return str(self.v3_impact_json)
class CVEV2Impact(models.Model):
    # cvssv2
    # vector_string = models.CharField(max_length=455)
    # access_vector = models.CharField(max_length=455)
    # access_complexity = models.CharField(max_length=455)
    # authentication = models.CharField(max_length=455)
    # confidentiality_impact = models.CharField(max_length=455)
    # integrity_impact = models.CharField(max_length=455)
    # availability_impact = models.CharField(max_length=455)
    # base_score = models.CharField(max_length=455)
    # # the rest
    # severity = models.CharField(max_length=455)
    # exploitability_score = models.CharField(max_length=455)
    # impact_score = models.CharField(max_length=455)
    # ac_insuf_info = models.CharField(max_length=455)
    # obtain_all_privilege = models.CharField(max_length=455)
    # obtain_user_privilege = models.CharField(max_length=455)
    # obtain_other_privilege = models.CharField(max_length=455)
    # user_interaction_required = models.CharField(max_length=455)
    v2_impact_json = JSONField()

    # Foreign keys
    cve = models.ForeignKey(NISTCVE, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'cvev2_impact'

    def __str__(self):
        return str(self.v2_impact_json)