# Generated by Django 2.1.7 on 2019-04-27 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0010_auto_20190424_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cvev2impact',
            old_name='v2_impact_json',
            new_name='impact_json',
        ),
        migrations.RenameField(
            model_name='cvev3impact',
            old_name='v3_impact_json',
            new_name='impact_json',
        ),
    ]
