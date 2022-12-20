# Generated by Django 4.1.4 on 2022-12-20 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('userID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=150)),
                ('time', models.DateTimeField()),
                ('partySize', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('userID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=300)),
                ('totalCost', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('userID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=150)),
                ('pickupTime', models.DateTimeField()),
                ('totalCost', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
