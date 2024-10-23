# Generated by Django 3.2.24 on 2024-10-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('number', models.CharField(max_length=150, verbose_name='Номер телефона')),
                ('e_mail', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Замер',
                'verbose_name_plural': 'Замеры',
            },
        ),
    ]
