# Generated by Django 2.2.4 on 2019-08-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='clients_photos'),
        ),
    ]