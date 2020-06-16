# Generated by Django 3.0.5 on 2020-04-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200428_2103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='text',
            new_name='maintext',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='maintext_en',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='maintext_zh_tw',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
