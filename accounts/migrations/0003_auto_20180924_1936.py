# Generated by Django 2.0.7 on 2018-09-24 16:36

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180921_1754'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('medina', django.db.models.manager.Manager()),
            ],
        ),
    ]