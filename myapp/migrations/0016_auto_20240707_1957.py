# Generated by Django 3.1.8 on 2024-07-07 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_item_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='use_extention',
            new_name='use_extenstion',
        ),
    ]
