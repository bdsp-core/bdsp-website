# Generated by Django 2.2.24 on 2022-01-05 17:19

from django.db import migrations


class Migration(migrations.Migration):
    MIGRATE_AFTER_INSTALL = True

    dependencies = [
        ('project', '0048_auto_20220105_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activeproject',
            name='is_self_managed_access',
        ),
        migrations.RemoveField(
            model_name='activeproject',
            name='self_managed_dua',
        ),
        migrations.RemoveField(
            model_name='activeproject',
            name='self_managed_request_template',
        ),
        migrations.RemoveField(
            model_name='archivedproject',
            name='is_self_managed_access',
        ),
        migrations.RemoveField(
            model_name='archivedproject',
            name='self_managed_dua',
        ),
        migrations.RemoveField(
            model_name='archivedproject',
            name='self_managed_request_template',
        ),
        migrations.RemoveField(
            model_name='publishedproject',
            name='is_self_managed_access',
        ),
        migrations.RemoveField(
            model_name='publishedproject',
            name='self_managed_dua',
        ),
        migrations.RemoveField(
            model_name='publishedproject',
            name='self_managed_request_template',
        ),
    ]
