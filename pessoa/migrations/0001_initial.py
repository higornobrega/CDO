# Generated by Django 2.2.4 on 2019-08-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(blank=True, max_length=100, null=True)),
                ('graduacao', models.CharField(blank=True, max_length=100, null=True)),
                ('peso', models.DecimalField(decimal_places=3, max_digits=6)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=3)),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
