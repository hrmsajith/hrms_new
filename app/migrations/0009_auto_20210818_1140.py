# Generated by Django 3.2.5 on 2021-08-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210817_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_restrictions',
            name='leave_cannot_taken_with',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leave_restrictions',
            name='leave_only_on',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leave_restrictions',
            name='leave_request_apply_check',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leave_restrictions',
            name='leave_request_apply_count',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leave_restrictions',
            name='leave_request_future_days',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leave_restrictions',
            name='leave_request_next_check',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leave_restrictions',
            name='leave_request_next_count',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leave_restrictions',
            name='leave_request_past_days',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leave_restrictions',
            name='maximum_application_period',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leave_restrictions',
            name='past_days_check',
            field=models.CharField(blank=True, default=0, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='leave_restrictions',
            name='past_days_count',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
