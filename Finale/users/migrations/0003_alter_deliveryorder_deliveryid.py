# Generated by Django 4.1.4 on 2023-05-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_deliveryorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryorder',
            name='deliveryID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
