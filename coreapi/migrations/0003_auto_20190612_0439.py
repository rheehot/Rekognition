# Generated by Django 2.2.1 on 2019-06-12 04:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coreapi', '0002_auto_20190612_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputimage',
            name='created_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='inputvideo',
            name='created_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
