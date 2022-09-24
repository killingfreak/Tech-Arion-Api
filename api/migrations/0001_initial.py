# Generated by Django 3.2 on 2022-09-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='site1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=50)),
                ('pro_image', models.ImageField(upload_to='')),
                ('pro_quantity', models.IntegerField()),
                ('pro_size', models.CharField(choices=[('1', 'Large'), ('2', 'medium'), ('3', 'small')], default='small', max_length=20)),
                ('pro_discription', models.TextField()),
                ('pro_star', models.IntegerField()),
            ],
        ),
    ]