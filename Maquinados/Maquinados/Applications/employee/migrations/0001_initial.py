# Generated by Django 4.1.2 on 2022-10-23 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eps_name', models.CharField(max_length=20, verbose_name='EPS')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client.person')),
                ('document', models.CharField(max_length=20, unique=True, verbose_name='Document')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('birthdate', models.DateField(verbose_name='Birthday')),
                ('eps_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.eps', verbose_name='EPS')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.position', verbose_name='Position')),
            ],
            options={
                'abstract': False,
            },
            bases=('client.person',),
        ),
    ]
