# Generated by Django 3.0.4 on 2021-04-15 05:19

from django.db import migrations, models
import website.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210414_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Find',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='0jpg')),
            ],
        ),
        migrations.AlterField(
            model_name='uploader',
            name='image_l',
            field=models.ImageField(blank=True, null=True, upload_to=website.models.path_and_rename),
        ),
    ]
