# Generated by Django 4.1.2 on 2023-06-15 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='plane',
            field=models.ImageField(upload_to='media'),
        ),
    ]