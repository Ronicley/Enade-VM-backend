# Generated by Django 2.1.2 on 2018-10-25 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma_api', '0004_auto_20181025_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ft_resultado',
            old_name='id_ano',
            new_name='ano',
        ),
    ]
