# Generated by Django 2.2 on 2018-10-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20181001_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treino',
            name='data_fim',
            field=models.DateField(blank=True, null=True, verbose_name='Data Fim'),
        ),
    ]
