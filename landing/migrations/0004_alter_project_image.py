# Generated by Django 4.2.3 on 2023-09-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='landing/static/landing/project_images/'),
        ),
    ]
