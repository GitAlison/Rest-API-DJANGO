# Generated by Django 2.2 on 2018-09-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180928_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cidade',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='frase',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Frase'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='uf',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Estado'),
        ),
    ]