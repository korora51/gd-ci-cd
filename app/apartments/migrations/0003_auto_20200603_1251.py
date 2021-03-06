# Generated by Django 3.0.6 on 2020-06-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_auto_20200603_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='city',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='floor',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='region',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='rooms',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='apartments',
            name='square_live',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5),
        ),
    ]
