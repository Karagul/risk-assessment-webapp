from django.db import models


# NIST choicest models--------------------------------------------------------------------
class NISTVendorOption(models.Model):
    name = models.CharField(max_length=255)
    note = models.TextField(max_length=255, blank=True, null=True)


    def import_nist_data(self):
        """ Imports NIST options data from formatted csv file into django NIST data models """
        import csv
        from applications.models import NISTApplicationOption

        with open('C:/Users/Derek/Desktop/Final Project/nist_cpe_raw_split.csv') as f:
            reader = csv.reader(f)
            vendor_count = 0
            h_count = 0
            a_count = 0
            o_count = 0
            for row in reader:
                #get unique vendors
                if row[0] != 'cpe_version': #Check if column header
                    #get vendor for row first
                    new_nist_vendor, created = NISTVendorOption.objects.get_or_create(
                        name=row[3],
                        note='',
                    )
                    if created:
                        vendor_count += 1
                    # if hardware
                    if row[2] == 'h':
                        # create nist hardware option
                        new_nist_hardware, created = NISTHardwareOption.objects.get_or_create(
                            product=row[4],
                            version=row[5],
                            update=row[6],
                            edition=row[7],
                            sw_edition=row[8],
                            target_sw=row[9],
                            target_hw=row[10],
                            language=row[11],
                            other=row[12],
                            vendor=new_nist_vendor
                        )
                        if created:
                            h_count += 1
                    # if app
                    if row[2] == 'a':
                        new_nist_application, created = NISTApplicationOption.objects.get_or_create(
                            product=row[4],
                            version=row[5],
                            update=row[6],
                            edition=row[7],
                            sw_edition=row[8],
                            target_sw=row[9],
                            target_hw=row[10],
                            language=row[11],
                            other=row[12],
                            vendor=new_nist_vendor
                        )
                        if created:
                            a_count += 1
                    # if os
                    if row[2] == 'o':
                        # create nist os option
                        new_nist_os, created = NISTOperatingSystemOption.objects.get_or_create(
                            product=row[4],
                            version=row[5],
                            update=row[6],
                            edition=row[7],
                            sw_edition=row[8],
                            target_sw=row[9],
                            target_hw=row[10],
                            language=row[11],
                            other=row[12],
                            vendor=new_nist_vendor
                        )
                        if created:
                            o_count += 1
            print('vendor count: ', vendor_count)
            print('h count: ', h_count)
            print('o count: ', o_count)
            print('a count: ', a_count)

    class Meta:
        db_table = 'nist_vendor_option'

    def __str__(self):
        return self.name
class NISTHardwareOption(models.Model):
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
        db_table = 'nist_hardware_option'

    def __str__(self):
        return str(self.product + ' ' + self.version + ' ' + self.update)

class NISTOperatingSystemOption(models.Model):
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
        db_table = 'nist_operating_system_option'

    def __str__(self):
        return str(self.product + ' ' + self.version + ' ' + self.update)

# NIST choicest models--------------------------------------------------------------------END
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    note = models.TextField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'vendor'

    def __str__(self):
        return self.name

class OperatingSystem(models.Model):
    label = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    note = models.TextField(max_length=255)

    # product = models.CharField(max_length=255)
    # version = models.CharField(max_length=255)
    # update = models.CharField(max_length=255, blank=True, null=True)
    # edition = models.CharField(max_length=255, blank=True, null=True)
    # sw_edition = models.CharField(max_length=255, blank=True, null=True)
    # target_sw = models.CharField(max_length=255, blank=True, null=True)
    # target_hw = models.CharField(max_length=255, blank=True, null=True)
    # language = models.CharField(max_length=255, blank=True, null=True)
    # other = models.CharField(max_length=255, blank=True, null=True)

    # calc field
    cpe_string = models.CharField(max_length=255, blank=True, null=True)

    vendor = models.ForeignKey(NISTVendorOption, on_delete=models.CASCADE)
    operating_system = models.ForeignKey(NISTOperatingSystemOption, on_delete=models.CASCADE)

    class Meta:
        db_table = 'operating_system'

    def __str__(self):
        return self.label

class Hardware(models.Model):
    label = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    note = models.TextField(max_length=255)
    #calc field, maybe make property
    cpe_string = models.CharField(max_length=255, blank=True, null=True)
    # NIST options
    vendor = models.ForeignKey(NISTVendorOption, on_delete=models.CASCADE)
    hardware = models.ForeignKey(NISTHardwareOption, on_delete=models.CASCADE)
    # Foreign keys
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)

    class Meta:
        db_table = 'hardware'

    def __str__(self):
        return self.label
        