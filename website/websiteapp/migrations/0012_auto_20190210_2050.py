# Generated by Django 2.1.5 on 2019-02-10 19:50

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0011_auto_20190210_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_article',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='order_of_appearance_on_website',
            field=models.IntegerField(),
        ),
    ]
