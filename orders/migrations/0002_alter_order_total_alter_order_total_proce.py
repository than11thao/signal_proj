# Generated by Django 4.2.2 on 2023-06-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_proce',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]