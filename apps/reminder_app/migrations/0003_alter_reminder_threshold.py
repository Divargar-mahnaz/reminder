# Generated by Django 3.2.3 on 2022-11-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder_app', '0002_alter_reminder_threshold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='threshold',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Threshold'),
        ),
    ]
