# Generated by Django 4.0.2 on 2022-02-19 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_scoring', '0007_alter_score_candidate_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='candidate_ref',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='candidate_scoring.candidate'),
        ),
    ]
