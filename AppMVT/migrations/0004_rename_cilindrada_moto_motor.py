# Generated by Django 4.1 on 2022-09-04 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMVT', '0003_alter_auto_motor_alter_camioneta_motor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moto',
            old_name='cilindrada',
            new_name='motor',
        ),
    ]
