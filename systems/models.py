from django.db import models

from hardware.models import Hardware

# Create your models here.
class System(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    is_third_party = models.BooleanField(default=False)

    # Foreign keys
    hardware = models.ManyToManyField(Hardware)
    #add system role


    class Meta:
        db_table = 'system'

    def __str__(self):
        return self.name
    
    @property
    def vuln_count(self):
        """ Gets sum of hardware, os, and app vulns for system """
        system_vuln_count = 0

        #get system apps vuln count
        s_app_vuln_count = self.apps_vuln_count()
        #get system hardware vuln count
        s_hardware_vuln_count = self.hardware_vuln_count()
        #get system os vuln count
        s_os_vuln_count = self.os_vuln_count()

        system_vuln_count = s_app_vuln_count + s_hardware_vuln_count + s_os_vuln_count

        return system_vuln_count
    
    def apps_vuln_count(self):
        app_vuln_count = 0
        sys_hardware = self.hardware.all()
        for hardware in sys_hardware:
            hardware_apps = hardware.application_set.all()
            for application in hardware_apps:
                app_vuln_count += application.vulnerability.count()

        return app_vuln_count

    def hardware_vuln_count(self):
        hardware_vuln_count = 0
        sys_hardware = self.hardware.all()
        for hardware in sys_hardware:
            hardware_vuln_count += hardware.vulnerability.count()
        
        return hardware_vuln_count

    def os_vuln_count(self):
        os_vuln_count = 0
        sys_hardware = self.hardware.all()
        for hardware in sys_hardware:
            os_vuln_count += hardware.operating_system.vulnerability.count()

        return os_vuln_count
