# Generated by Django 3.0.2 on 2020-02-04 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20200204_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomType', models.CharField(max_length=111)),
                ('Check_In', models.TextField()),
                ('Check_Out', models.TextField()),
                ('Adults', models.IntegerField(null='True')),
                ('Children', models.IntegerField(null='True')),
            ],
        ),
    ]
