# Generated by Django 3.2.8 on 2021-12-11 12:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_auto_20211202_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.IntegerField(default='')),
                ('county', models.CharField(default='', max_length=30)),
                ('state', models.CharField(default='', max_length=30)),
                ('massage', models.CharField(default='', max_length=30)),
                ('datetime', models.DateTimeField(verbose_name=datetime.datetime(2021, 12, 11, 12, 15, 7, 842977, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]