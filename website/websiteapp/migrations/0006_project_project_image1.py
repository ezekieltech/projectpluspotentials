# Generated by Django 2.1.5 on 2019-02-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0005_auto_20190127_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_image1',
            field=models.ImageField(default='projectimages/None/no-img.jpg', upload_to='projectimages/'),
        ),
    ]
