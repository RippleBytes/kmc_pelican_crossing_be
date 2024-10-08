# Generated by Django 5.1.1 on 2024-10-01 01:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_roadwayfacilitynear_electric_poles_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadwayfacilityfar',
            name='electric_poles_latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilityfar',
            name='electric_poles_longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilityfar',
            name='street_side_one_latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilityfar',
            name='street_side_one_longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilityfar',
            name='street_side_two_latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilityfar',
            name='street_side_two_longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='roadwayfacilityfar',
            name='school',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.school'),
        ),
        migrations.AlterField(
            model_name='roadwayfacilitynear',
            name='footpath',
            field=models.CharField(choices=[('None', 'None'), ('Both-Side', 'Both-Side'), ('One-Side', 'One-Side')], max_length=100),
        ),
        migrations.AlterField(
            model_name='roadwayfacilitynear',
            name='school',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.school'),
        ),
    ]
