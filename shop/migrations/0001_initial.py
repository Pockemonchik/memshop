

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('profiles', '0001_initial'),

        ('profiles', '0003_auto_20190124_2056'),

    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='mem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disctiption', models.TextField()),
                ('mem_img', models.ImageField(blank=True, null=True, upload_to='mems')),
                ('cost', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=200)),
                ('available', models.BooleanField(default=False)),

                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mems_of_profile', to='profiles.UserProfile')),

                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mems_of_profile', to='profiles.UserProfile')),

                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mem', to='shop.Category')),
            ],
        ),
        migrations.AlterIndexTogether(
            name='mem',
            index_together={('id', 'slug')},
        ),
    ]
