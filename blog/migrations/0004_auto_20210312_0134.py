# Generated by Django 3.1.7 on 2021-03-12 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('blog', '0003_auto_20210309_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='blog_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
