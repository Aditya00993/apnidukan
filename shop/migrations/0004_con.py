# Generated by Django 4.1.7 on 2024-06-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_ram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Con',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=25)),
                ('message', models.CharField(max_length=350)),
            ],
        ),
    ]
