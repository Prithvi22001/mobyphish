# Generated by Django 5.0.6 on 2024-06-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_location_item_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='all_info',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='item',
            name='results',
            field=models.JSONField(default=dict),
        ),
    ]
