# Generated by Django 3.2.5 on 2021-09-30 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_organization_files_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization_files',
            name='folder',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.CreateModel(
            name='Employee_Files',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(max_length=254, upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.PositiveSmallIntegerField(default=1)),
                ('device', models.CharField(blank=True, max_length=20, null=True)),
                ('folder', models.CharField(blank=True, max_length=1000, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_files_added', to='app.employee')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_id_files', to='app.employee')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_files_updated', to='app.employee')),
            ],
            options={
                'db_table': 'employee_files',
            },
        ),
    ]