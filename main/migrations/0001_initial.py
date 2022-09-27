# Generated by Django 4.1.1 on 2022-09-27 08:16

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColorTone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('code', models.CharField(max_length=512)),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='SubProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=512)),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='TypeAndPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('sub_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='main.subproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(max_length=512)),
                ('image', models.ImageField(blank=True, null=True, upload_to=main.models.upload_to)),
                ('sub_products', models.ManyToManyField(to='main.subproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=512)),
                ('email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=512)),
                ('slogan', models.CharField(max_length=512)),
                ('color_tone', models.ManyToManyField(to='main.colortone')),
                ('industry', models.ManyToManyField(to='main.industry')),
                ('type_and_preferences', models.ManyToManyField(to='main.typeandpreferences')),
            ],
        ),
    ]
