# Generated by Django 4.0.5 on 2022-07-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=50)),
                ('budget', models.CharField(max_length=50)),
                ('event_type', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]