# Generated by Django 4.2 on 2023-05-08 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_remove_user_patronymic_remove_user_surname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=254, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=254, unique=True, verbose_name='phone_number'),
        ),
    ]
