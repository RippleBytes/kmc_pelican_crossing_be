# Generated by Django 5.1.1 on 2024-09-30 11:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_school_bus_ownership_alter_school_school_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roadwayfacilitynear',
            old_name='foot_over_bridge_picture',
            new_name='foot_over_bridge_pic_one',
        ),
        migrations.RenameField(
            model_name='roadwayfacilitynear',
            old_name='traffic_lights_pictures',
            new_name='foot_over_bridge_pic_three',
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='carriage_way_direction',
            field=models.CharField(choices=[('One-Way', 'One-Way'), ('Two-Way', 'Two-Way')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='foot_over_bridge_one_latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='foot_over_bridge_one_longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='foot_over_bridge_pic_two',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='foot_over_bridge_three_latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='foot_over_bridge_three_longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='foot_over_bridge_two_latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='foot_over_bridge_two_longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='is_partial_one_way',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='is_partial_two_way',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='partial_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='partial_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='traffic_lights_pic_one',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='traffic_lights_pic_three',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='roadwayfacilitynear',
            name='traffic_lights_pic_two',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
