# Generated by Django 2.1.2 on 2018-12-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20181221_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mem',
            name='mem_img',
            field=models.ImageField(blank=True, null=True, upload_to='mems'),
        ),
    ]