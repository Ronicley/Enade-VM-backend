# Generated by Django 2.1.2 on 2019-05-26 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma_api', '0012_remove_ft_associacao_suporte'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ft_associacao',
            old_name='antecedente',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ft_associacao',
            old_name='total',
            new_name='value',
        ),
        migrations.RemoveField(
            model_name='ft_associacao',
            name='consequente',
        ),
    ]
