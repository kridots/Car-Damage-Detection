# Generated by Django 4.2.11 on 2024-03-18 13:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("car_image_detect", "0002_emailcruddata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailcruddata",
            name="subject",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]