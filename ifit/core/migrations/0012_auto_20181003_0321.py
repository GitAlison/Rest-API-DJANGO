# Generated by Django 2.2 on 2018-10-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20181002_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='foto',
            field=models.ImageField(blank='true', default='media/user/perfil/avatar.png', upload_to='user/perfil', verbose_name='Foto Perfil'),
        ),
    ]
