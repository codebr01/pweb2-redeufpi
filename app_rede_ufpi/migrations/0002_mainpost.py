# Generated by Django 4.2.6 on 2023-12-09 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_rede_ufpi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_rede_ufpi.user')),
            ],
        ),
    ]
