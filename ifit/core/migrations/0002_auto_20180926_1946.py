# Generated by Django 2.2 on 2018-09-26 22:46

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data da solicitacao')),
            ],
        ),
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_customuser_friends_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Solicitacao',
        ),
        migrations.AddField(
            model_name='convite',
            name='convidado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_recebidos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='convite',
            name='convidante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criador_convite', to=settings.AUTH_USER_MODEL),
        ),
    ]
