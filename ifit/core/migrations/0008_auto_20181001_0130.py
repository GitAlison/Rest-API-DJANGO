# Generated by Django 2.2 on 2018-10-01 04:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180930_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='data_end',
        ),
        migrations.RemoveField(
            model_name='avaliacao',
            name='data_start',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='data_create',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de criação'),
            preserve_default=False,
        ),
    ]
