# Generated by Django 4.2.7 on 2023-11-28 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0018_rename_sale_salesdetail_folio_remove_sale_folio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesdetail',
            old_name='folio',
            new_name='sale',
        ),
    ]
