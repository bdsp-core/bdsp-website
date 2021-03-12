# Generated by Django 2.2.13 on 2021-02-12 18:06

from django.db import migrations, models
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0032_orcid'),
    ]

    operations = [
        migrations.AddField(
            model_name='credentialapplication',
            name='reference_organization',
            field=models.CharField(blank=True, max_length=200, validators=[user.validators.validate_organization]),
        ),
    ]