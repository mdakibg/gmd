# Generated by Django 3.1.2 on 2021-01-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20210117_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Flooring & Staircase', 'Flooring & Staircase'), ('Carving', 'Carving'), ('Home & Garden Decor', 'Home & Garden Decor'), ('Inlay', 'Inlay'), ('Home Mandir', 'Home Mandir'), ('Wall Cladding', 'Wall Cladding'), ('Qibla & Mimbar', 'Qibla & Mimbar'), ('Jali', 'Jali'), ('Katera & Kabr', 'Katera & Kabr'), ('Railing', 'Railing'), ('Name Plate', 'Name Plate')], max_length=20),
        ),
    ]
