# Generated by Django 4.2.6 on 2023-12-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_rede_ufpi', '0002_mainpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]