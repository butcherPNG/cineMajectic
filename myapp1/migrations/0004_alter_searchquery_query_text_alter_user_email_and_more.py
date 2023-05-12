# Generated by Django 4.2 on 2023-05-07 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_rename_created_at_searchquery_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchquery',
            name='query_text',
            field=models.CharField(default='Введите адрес', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=254, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=254, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(blank=True, max_length=254, verbose_name='patromymic'),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=254, verbose_name='surname'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=254, unique=True, verbose_name='login'),
        ),
    ]
