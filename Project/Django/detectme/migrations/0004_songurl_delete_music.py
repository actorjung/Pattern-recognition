# Generated by Django 4.1.3 on 2022-12-08 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detectme', '0003_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myunknowncolumn', models.TextField(blank=True, db_column='MyUnknownColumn', null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('issue_date', models.TextField(blank=True, null=True)),
                ('album_name', models.TextField(blank=True, null=True)),
                ('artist_name_basket', models.TextField(blank=True, null=True)),
                ('song_name', models.TextField(blank=True, null=True)),
                ('song_url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'song_url',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Music',
        ),
    ]
