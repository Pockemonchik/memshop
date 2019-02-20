# Generated by Django 2.1.5 on 2019-02-11 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_mem_mem_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mem',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mems_of_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]