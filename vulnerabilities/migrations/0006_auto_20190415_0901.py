# Generated by Django 2.1.7 on 2019-04-15 15:01

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0005_auto_20190414_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVEReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('cve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.NISTCVE')),
            ],
            options={
                'db_table': 'cve_reference',
            },
        ),
        migrations.CreateModel(
            name='CVEV2Impact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vector_string', models.CharField(max_length=255)),
                ('access_vector', models.CharField(max_length=255)),
                ('access_complexity', models.CharField(max_length=255)),
                ('authentication', models.CharField(max_length=255)),
                ('confidentiality_impact', models.CharField(max_length=255)),
                ('integrity_impact', models.CharField(max_length=255)),
                ('availability_impact', models.CharField(max_length=255)),
                ('base_score', models.CharField(max_length=255)),
                ('severity', models.CharField(max_length=255)),
                ('exploitability_score', models.CharField(max_length=255)),
                ('impact_score', models.CharField(max_length=255)),
                ('ac_insuf_info', models.CharField(max_length=255)),
                ('obtain_all_privilege', models.CharField(max_length=255)),
                ('obtain_user_privilege', models.CharField(max_length=255)),
                ('obtain_other_privilege', models.CharField(max_length=255)),
                ('user_interaction_required', models.CharField(max_length=255)),
                ('cve', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.NISTCVE')),
            ],
            options={
                'db_table': 'cvev2_impact',
            },
        ),
        migrations.CreateModel(
            name='CVEV3Impact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vector_string', models.CharField(max_length=255)),
                ('attack_vector', models.CharField(max_length=255)),
                ('attack_complexity', models.CharField(max_length=255)),
                ('privileges_required', models.CharField(max_length=255)),
                ('user_interaction', models.CharField(max_length=255)),
                ('scope', models.CharField(max_length=255)),
                ('confidentiality_impact', models.CharField(max_length=255)),
                ('integrity_impact', models.CharField(max_length=255)),
                ('availability_impact', models.CharField(max_length=255)),
                ('base_score', models.CharField(max_length=255)),
                ('base_severity', models.CharField(max_length=255)),
                ('exploitability_score', models.CharField(max_length=255)),
                ('impact_score', models.CharField(max_length=255)),
                ('cve', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vulnerabilities.NISTCVE')),
            ],
            options={
                'db_table': 'cvev3_impact',
            },
        ),
        migrations.CreateModel(
            name='VulnerableCPE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpe_json', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'db_table': 'vulnerable_cpe',
            },
        ),
        migrations.AddField(
            model_name='nistcve',
            name='vulnerable_cpe',
            field=models.ManyToManyField(to='vulnerabilities.VulnerableCPE'),
        ),
    ]
