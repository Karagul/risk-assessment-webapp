# Generated by Django 2.1.7 on 2019-04-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0006_auto_20190415_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvereference',
            name='name',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvereference',
            name='source',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvereference',
            name='url',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='ac_insuf_info',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='access_complexity',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='access_vector',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='authentication',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='availability_impact',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='base_score',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='confidentiality_impact',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='exploitability_score',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='impact_score',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='integrity_impact',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='obtain_all_privilege',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='obtain_other_privilege',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='obtain_user_privilege',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='severity',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='user_interaction_required',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev2impact',
            name='vector_string',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='attack_complexity',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='attack_vector',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='availability_impact',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='base_score',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='base_severity',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='confidentiality_impact',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='exploitability_score',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='impact_score',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='integrity_impact',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='privileges_required',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='scope',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='user_interaction',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='cvev3impact',
            name='vector_string',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='nistcve',
            name='cve_id',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='nistcve',
            name='date_modified',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='nistcve',
            name='date_published',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='nistcve',
            name='description',
            field=models.TextField(max_length=455),
        ),
    ]
