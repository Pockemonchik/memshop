# Generated by Django 2.1.2 on 2018-12-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181212_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mem',
            name='mem_img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]