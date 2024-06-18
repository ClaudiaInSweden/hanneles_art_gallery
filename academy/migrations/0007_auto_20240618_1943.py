# Generated by Django 3.2.24 on 2024-06-18 19:43

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0006_auto_20240618_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bodytext',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
    ]
