from django.db import models
from django.db.models import Q

# Create your models here.
from hardware.models import NISTVendorOption, Hardware
from vulnerabilities.models import Vulnerability

from ares import CVESearch

# NIST choices models--------------------------------------------------------------------
class NISTApplicationOption(models.Model):
    product = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    update = models.CharField(max_length=255, blank=True, null=True)
    edition = models.CharField(max_length=255, blank=True, null=True)
    sw_edition = models.CharField(max_length=255, blank=True, null=True)
    target_sw = models.CharField(max_length=255, blank=True, null=True)
    target_hw = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)

    vendor = models.ForeignKey(NISTVendorOption, on_delete=models.CASCADE)


    class Meta:
        db_table = 'nist_application_option'

    def __str__(self):
        return str('cpe:2.3:a:' + str(self.vendor) + ':' + self.product + ':' + self.version + ':' + self.update + ':' + self.edition + ':' + self.language + ':' + self.sw_edition + ':' + self.target_sw + ':' + self.target_hw + ':' + self.other)

    def get_cves(self):
        from vulnerabilities.models import NISTCVE
        from packaging import version
        v = None
        # use product and version to search via api
        # get cve ids from response
        # query local db for cve_id
        # 
        # return
        base_url = 'https://cve.circl.lu/api/cvefor/'
        cpe_string = 'cpe:2.3:a:' + str(self.vendor) + ':' + self.product + ':' + self.version
        
        cve = CVESearch()
        # result = cve.search(str(self.vendor) + '/' + self.product)
        result = cve.cvefor(base_url + cpe_string)
        # https://cve.circl.lu/api/cvefor/cpe:2.3:a:apache:http_server:2.4.37


        return result
# NIST choicest models--------------------------------------------------------------------END

class Application(models.Model):
    label = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    note = models.TextField(max_length=255)

    #calc field, maybe make property
    cpe_string = models.CharField(max_length=255, blank=True, null=True)

    # product = models.CharField(max_length=50)
    # version = models.CharField(max_length=255)
    # update = models.CharField(max_length=255, blank=True, null=True)
    # edition = models.CharField(max_length=255, blank=True, null=True)
    # sw_edition = models.CharField(max_length=255, blank=True, null=True)
    # target_sw = models.CharField(max_length=255, blank=True, null=True)
    # target_hw = models.CharField(max_length=255, blank=True, null=True)
    # language = models.CharField(max_length=255, blank=True, null=True)
    # other = models.CharField(max_length=255, blank=True, null=True)

    #NIST stuff
    vendor = models.ForeignKey(NISTVendorOption, on_delete=models.CASCADE)
    application = models.ForeignKey(NISTApplicationOption, on_delete=models.CASCADE)

    # Foreign keys
    hardware = models.ManyToManyField(Hardware)
    vulnerability = models.ManyToManyField(Vulnerability)


    class Meta:
        db_table = 'application'

    def __str__(self):
        return self.label

    def cve_getter(self):
        cve_dict = self.application.get_cves()
        for cve in cve_dict:
            # print(cve['Modified'])
            # print(cve['Published'])
            # print(cve['id'])
            # print(cve['summary'])
            vuln, created = Vulnerability.objects.get_or_create(
                cve_json=cve
            )
            self.vulnerability.add(vuln)

        return True



# ONLY CREATE REPORT ONCE PROCESS_COMPLETE()==TRUE
# reports

# call check_process_complete()
# create pdf from survey model data
# save pdf to report model and associate with user/session
# display download link of pdf, require password for download
# Upon download show message prompting if data should be deleted from server or auto delete in mins
# delete sensitive model data at appropriate time
    # name
    ########FKeys##########
    # application
    # hardware
    # system
    # activity
    # role
    # 
    ##########Don't Need#########