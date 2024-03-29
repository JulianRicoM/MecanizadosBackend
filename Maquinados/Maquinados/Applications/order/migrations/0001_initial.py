# Generated by Django 4.1.2 on 2023-05-02 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quote', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(max_length=20, verbose_name='Currency')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProcess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_process', models.CharField(max_length=20, verbose_name='Order Process')),
                ('order_process', models.CharField(max_length=20, verbose_name='Order Status')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_name', models.CharField(max_length=20, verbose_name='Payment')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Discount')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subtotal')),
                ('freigth', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Freigth')),
                ('various_expenses', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Various Expenses')),
                ('amount_whitout_vat', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount Whitout VAT')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount')),
                ('delivery_address', models.CharField(max_length=40, verbose_name='Delivery Address')),
                ('status_id', models.BooleanField(default=False)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.currency', verbose_name='Currency')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee', verbose_name='Employee')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.paymentmethod', verbose_name='Payment Methods')),
                ('process_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orderprocess', verbose_name='Process')),
                ('quote_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.quote', verbose_name='Quote Number')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
