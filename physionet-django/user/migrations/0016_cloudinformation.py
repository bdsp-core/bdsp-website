# Generated by Django 2.1.9 on 2019-07-25 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20190709_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aws_id', models.CharField(default=None, max_length=60, null=True)),
                ('gcp_email', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gcp_email', to='user.AssociatedEmail')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cloud_information', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]