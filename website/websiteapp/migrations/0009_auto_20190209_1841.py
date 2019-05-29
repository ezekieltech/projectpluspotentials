# Generated by Django 2.1.5 on 2019-02-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0008_auto_20190208_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_passport',
            field=models.ImageField(default='staffimages/None/no-img.jpg', upload_to='staffimages/'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(help_text='Name of staff', max_length=50),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(help_text='Name of Job Position', max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='qualification',
            field=models.CharField(help_text='Enter Job Qualification', max_length=30),
        ),
    ]