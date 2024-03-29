# Generated by Django 4.1.2 on 2023-05-02 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement_units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('reference', models.CharField(max_length=30, verbose_name='Reference')),
                ('plane', models.FileField(upload_to='media')),
                ('surface_finish', models.CharField(max_length=15, verbose_name='Surface Finish')),
                ('tolerance', models.IntegerField(blank=True, null=True, verbose_name='Tolerance')),
                ('linear', models.IntegerField(blank=True, null=True, verbose_name='Linear')),
                ('angular', models.IntegerField(blank=True, null=True, verbose_name='Angular')),
                ('size', models.IntegerField(verbose_name='Size')),
                ('volume', models.IntegerField(verbose_name='Volume')),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.material', verbose_name='Material Type')),
                ('measurement_units_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.measurement_units')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
