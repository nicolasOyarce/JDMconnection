# Generated by Django 4.2.7 on 2023-11-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_rename_folio_salesdetail_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
