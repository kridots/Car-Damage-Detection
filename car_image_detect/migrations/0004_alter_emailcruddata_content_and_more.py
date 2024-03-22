# Generated by Django 4.2.11 on 2024-03-18 13:38

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_image_detect", "0003_alter_emailcruddata_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailcruddata",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name="emailcruddata",
            name="subject",
            field=models.CharField(max_length=255),
        ),
    ]
