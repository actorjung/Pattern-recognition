# Generated by Django 4.1.3 on 2022-11-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detectme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('uploadedFile', models.FileField(upload_to='Uploaded Files/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
