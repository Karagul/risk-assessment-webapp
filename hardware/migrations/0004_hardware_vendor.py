# Generated by Django 2.1.7 on 2019-03-20 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0003_auto_20190320_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hardware.NISTVendorOption'),
            preserve_default=False,
        ),
    ]
