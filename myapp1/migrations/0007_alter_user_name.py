# Generated by Django 4.2 on 2023-05-08 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0006_alter_user_name_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=254, unique=True, verbose_name='login'),
        ),
    ]