# Generated by Django 3.0.5 on 2020-05-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200509_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='billboard',
            name='textcolor',
            field=models.CharField(blank=True, help_text='Sets the text color on the billboard. Please provide the hex code: e.g. #000000. Is black by default.', max_length=7),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='headline',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='headline_en',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='headline_zh_tw',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='subtitle',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='subtitle_zh_tw',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='typewriter',
            field=models.BooleanField(default=True, help_text='To turn on / off typewriter effect on the billboard. Only works for the first billboard element (not for the other slides).'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(help_text='Does accept raw HTML text. e.g. for line breaks use <br>'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_en',
            field=models.TextField(help_text='Does accept raw HTML text. e.g. for line breaks use <br>', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_zh_tw',
            field=models.TextField(help_text='Does accept raw HTML text. e.g. for line breaks use <br>', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='subtitle',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='subtitle_zh_tw',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='headline',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='services',
            name='headline_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='headline_zh_tw',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='text_zh_tw',
            field=models.TextField(blank=True, null=True),
        ),
    ]