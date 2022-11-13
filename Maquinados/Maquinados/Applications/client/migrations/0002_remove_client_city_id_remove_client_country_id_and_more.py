# Generated by Django 4.1.2 on 2022-10-23 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='client',
            name='country_id',
        ),
        migrations.RemoveField(
            model_name='client',
            name='departament_id',
        ),
        migrations.AddField(
            model_name='person',
            name='city_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='client.city'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='country_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='client.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='departament_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='client.department'),
            preserve_default=False,
        ),
    ]