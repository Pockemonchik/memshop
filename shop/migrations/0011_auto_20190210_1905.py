# Generated by Django 2.1.5 on 2019-02-10 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_mem_mem_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mem',
            name='mem_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile'),
        ),
    ]