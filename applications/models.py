from django.db import models

# Create your models here.
from hardware.models import NISTVendorOption

# NIST choices models--------------------------------------------------------------------
class NISTApplicationOption(models.Model):
    product = models.CharField(max_length=50)
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
        return str(self.product + ' ' + self.version + ' ' + self.update)
# NIST choicest models--------------------------------------------------------------------END


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