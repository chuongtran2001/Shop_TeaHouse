# Generated by Django 4.2.7 on 2023-11-17 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appteahouse', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product', to='appteahouse.category'),
        ),
    ]
