# Generated by Django 4.1.2 on 2022-10-28 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_remove_client_city_id_remove_client_country_id_and_more'),
        ('quote', '0004_alter_quote_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='client_id',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Client'),
        ),
    ]