# Generated by Django 2.2 on 2018-09-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180928_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciciotreino',
            name='carga',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='Carga'),
        ),
    ]
