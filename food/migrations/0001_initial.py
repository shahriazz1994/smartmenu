# Generated by Django 2.1.3 on 2018-11-23 11:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=100)),
                ('categorydetails', models.CharField(max_length=1000)),
                ('categoryimage', models.ImageField(default='cat_def.jpg', upload_to='catimg')),
            ],
            options={
                'verbose_name': 'Food Category',
            },
        ),
        migrations.CreateModel(
            name='FoodDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=100)),
                ('fooddetails', models.CharField(max_length=1000)),
                ('foodimage', models.ImageField(default='food_def.jpg', upload_to='fodimg')),
                ('armodel', models.CharField(default='andy.sfb', max_length=50)),
                ('additiondate', models.DateTimeField(default=django.utils.timezone.now)),
                ('longdetails', models.CharField(max_length=1000)),
                ('fromcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.FoodCategory')),
            ],
            options={
                'verbose_name': 'Food Detail',
            },
        ),
    ]