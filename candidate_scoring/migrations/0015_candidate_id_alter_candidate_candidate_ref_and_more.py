# Generated by Django 4.0.2 on 2022-02-19 15:07

import candidate_scoring.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_scoring', '0014_remove_candidate_id_alter_candidate_candidate_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidate_ref',
            field=models.CharField(default=1, max_length=8, unique=True, validators=[candidate_scoring.models.validator_ref], verbose_name='Candidate Reference'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(default=1, max_length=60, verbose_name='Candidate Name'),
        ),
        migrations.AlterField(
            model_name='score',
            name='candidate_ref',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='candidate_scoring.candidate'),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.FloatField(default=1, validators=[candidate_scoring.models.validate_score], verbose_name='Candidate Score'),
        ),
    ]
