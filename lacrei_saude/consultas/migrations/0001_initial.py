# Generated by Django 5.1.1 on 2024-09-05 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255)),
                ('nome_social', models.CharField(blank=True, max_length=255, null=True)),
                ('profissao', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('contato', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.profissional')),
            ],
        ),
    ]
