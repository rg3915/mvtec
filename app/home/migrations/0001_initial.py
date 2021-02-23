# Generated by Django 3.1.3 on 2021-02-19 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70, verbose_name='Nome')),
                ('email', models.EmailField(max_length=90, verbose_name='Email')),
                ('assunto', models.CharField(max_length=120, verbose_name='Assunto')),
                ('mensagem', models.TextField(verbose_name='Mensagem')),
                ('status', models.CharField(choices=[('Lido', 'Lido'), ('Não Lido', 'Não Lido')], default='Não Lido', max_length=14)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
                'db_table': 'tb_mvt_contact',
            },
        ),
    ]
