# Generated by Django 4.1.2 on 2022-12-18 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_remove_client_city_id_remove_client_country_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='departament_id',
            new_name='department_id',
        ),
    ]
