# Generated by Django 4.2.7 on 2023-11-28 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0021_sale_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]
