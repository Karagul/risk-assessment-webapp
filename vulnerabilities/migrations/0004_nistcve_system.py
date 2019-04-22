# Generated by Django 2.1.7 on 2019-04-14 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0001_initial'),
        ('vulnerabilities', '0003_remove_nistcve_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='nistcve',
            name='system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='systems.System'),
        ),
    ]
