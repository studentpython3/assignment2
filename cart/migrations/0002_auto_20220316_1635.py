# Generated by Django 2.2 on 2022-03-16 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='items',
            name='prodt',
        ),
        migrations.DeleteModel(
            name='Cartlist',
        ),
        migrations.DeleteModel(
            name='items',
        ),
    ]