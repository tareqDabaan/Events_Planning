# Generated by Django 4.1.7 on 2023-08-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
