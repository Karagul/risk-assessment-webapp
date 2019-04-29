from django.db import models

# Create your models here.

class DataType(models.Model):
    """ 
    These are data type labels that are going to be used to assess what legal 
    requirements need to be meet for things like HIPAA, PCI, etc. 
    """
    #make choices for label - PII, Financial data, etc.,  
    label = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    note = models.TextField(max_length=255)
    # Foreign keys


    class Meta:
        db_table = 'data_type'

    def __str__(self):
        return self.label

class InfoAssetGroup(models.Model):
    label = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    note = models.TextField(max_length=255)

    confidentiality_requirement = models.CharField(max_length=255)
    integrity_requirement = models.CharField(max_length=255)
    availability_requirement = models.CharField(max_length=255)
    # Foreign keys
    data_types = models.ManyToManyField(DataType)


    class Meta:
        db_table = 'info_asset_group'

    def __str__(self):
        return self.label
    
    def num_vulns_impacting(self):
        """ get count of vulns where this data is present """
        vuln_count = 0
        system_list = []
        activities = self.systemactivity_set.all()

        # get list of systems
        for activity in activities:
            roles = activity.system_role.all()
            for role in roles:
                system_list.append(role.system)
        
        # sum vuln_counts
        for system in set(system_list):
            vuln_count += system.vuln_count

        return vuln_count
