# Generated by Django 5.2.4 on 2025-07-30 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_customer_user_type_vendor_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='Vendor',
            new_name='vendor',
        ),
    ]
