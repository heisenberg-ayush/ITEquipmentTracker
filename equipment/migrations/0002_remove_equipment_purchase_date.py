# Generated by Django 4.1.7 on 2023-04-25 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='purchase_date',
        ),
    ]
