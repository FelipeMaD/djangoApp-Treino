# Generated by Django 5.1.4 on 2025-01-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_email_cliente_idade_cliente_salario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]
