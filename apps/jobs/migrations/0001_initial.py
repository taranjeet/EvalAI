# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 18:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jobs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('challenges', '0007_rename_test_environment'),
        ('participants', '0007_add_team_participant'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('submitted', 'submitted'), ('running', 'running'), ('failed', 'failed'), ('cancelled', 'cancelled'), ('finished', 'finished')], max_length=30)),
                ('is_public', models.BooleanField(default=False)),
                ('submission_number', models.PositiveIntegerField(default=0)),
                ('download_count', models.IntegerField(default=0)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('when_made_public', models.DateTimeField(blank=True, null=True)),
                ('input_file', models.FileField(upload_to=jobs.models.input_file_name)),
                ('stdout_file', models.FileField(blank=True, null=True, upload_to=jobs.models.stdout_file_name)),
                ('stderr_file', models.FileField(blank=True, null=True, upload_to=jobs.models.stderr_file_name)),
                ('challenge_phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='challenges.ChallengePhase')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('participant_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='participants.ParticipantTeam')),
            ],
            options={
                'db_table': 'submission',
            },
        ),
    ]
