# Generated by Django 3.2.23 on 2024-01-19 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='format',
            field=models.CharField(max_length=20),
        ),
    ]
