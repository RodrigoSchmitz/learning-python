# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('contato_id', models.AutoField(primary_key=True, serialize=False)),
                ('contato_nome', models.CharField(max_length=50)),
                ('contato_nascimento', models.DateField()),
                ('contato_sexo', models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=50)),
                ('contato_estado_civil', models.CharField(choices=[('solterio', 'Solteiro'), ('casado', 'Casado'), ('divorciado', 'Divorciado'), ('viuvo', 'Viuvo')], max_length=50, verbose_name='Estado Civil')),
                ('contato_email', models.CharField(max_length=50)),
                ('contato_favorito', models.BooleanField(verbose_name='Favorito')),
            ],
        ),
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('tarefa_id', models.AutoField(primary_key=True, serialize=False)),
                ('tarefa_nome', models.CharField(max_length=120)),
                ('tarefa_data_inicio', models.DateField()),
                ('concluido', models.BooleanField(verbose_name='Concluido')),
            ],
        ),
    ]