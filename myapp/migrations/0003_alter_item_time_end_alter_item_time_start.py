# Generated by Django 5.0.6 on 2024-06-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_item_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time_end',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='time_start',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
