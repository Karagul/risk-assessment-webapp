from django.db import models

from systems.models import System
from django.contrib.postgres.fields import JSONField

class NISTCVE(models.Model):
    # d_version = models.CharField(max_length=255)
    # d_format = models.CharField(max_length=255)
    # cve_id = models.CharField(max_length=255)
    # cwe_id = models.CharField(max_length=255)
    # description = models.TextField(max_length=255)
    # date_published = models.CharField(max_length=255)
    # date_last_modified
    # note = models.TextField(max_length=255)
    date_pullled = models.DateTimeField('date pulled', auto_now=True)
    json_data = JSONField()

    # Foreign keys
    system = models.ForeignKey(System, on_delete=models.CASCADE, null=True, blank=True)

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
            print(cve_dict.keys())
            # d_version = models.CharField(max_length=255)
            print(cve_dict['CVE_data_version'])
            # d_format = models.CharField(max_length=255)
            print(cve_dict['CVE_data_format'])
            print(cve_dict['CVE_data_timestamp'])
            print(cve_dict['CVE_data_numberOfCVEs'])
            cve_dict_items = cve_dict['CVE_Items']
            # get cpe from json data
            # v2.json_data['configurations']['nodes'][0]['cpe_match'][0]['cpe23Uri']
            for cve in cve_dict['CVE_Items']:
                NISTCVE.objects.get_or_create(
                    json_data=cve
                )# #
                # # cve_id = models.CharField(max_length=255)
                # print(cve['cve']['CVE_data_meta']['ID'])
                # # cwe_id = models.CharField(max_length=255)
                # # description = models.TextField(max_length=255)
                # print(cve['cve']['description']['description_data'][0]['value'])
                # # date_published = models.CharField(max_length=255)
                # print(cve['publishedDate'])
                # print(cve['lastModifiedDate'])
                # # date_last_modified
                # # note = models.TextField(max_length=255)

    class Meta:
        db_table = 'nist_cve'

    def __str__(self):
        return str(self.json_data)

#tables to add
# references


# class CVEReference(models.Model):
    # url
    # name
    # tags

# class VulnerableCPE(models.Model):
    # vulnerable
    # cpe_uri
    # version_start
    # version_end

# class CVEImpact(models.Model):
    # version
    # vector_string
    # attack_vector
    # attack_complexity
    # privileges_required
    # user_interaction
    # scope
    # confidentiality_impact
    # integrity_impact
    # availability_impact
    # base_score
    # base_severity
    # exploitability_score
    # impact_score

    