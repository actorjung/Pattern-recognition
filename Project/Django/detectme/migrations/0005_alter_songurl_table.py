# Generated by Django 4.1.3 on 2022-12-09 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detectme', '0004_songurl_delete_music'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='songurl',
            table='song',
        ),
    ]
