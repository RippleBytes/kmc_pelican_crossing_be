# Generated by Django 5.1.1 on 2024-09-28 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_school_coordinates_school_school_coordinates_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoadwayFacilityFar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carriage_width', models.FloatField()),
                ('carriage_direction', models.CharField(choices=[('North-South', 'North-South'), ('East-West', 'East-West'), ('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')], max_length=20)),
                ('divided', models.CharField(choices=[('Undivided', 'Undivided'), ('Central Refuge', 'Central Refuge'), ('Barrier', 'Barrier')], max_length=20)),
                ('intersection_type', models.CharField(blank=True, choices=[('No-Intersection', 'No-Intersection'), ('T-Junction', 'T-Junction'), ('4-Legged-Intersection', '4-Legged-Intersection'), ('Y-Junction', 'Y-Junction'), ('Staggered-T-Junction', 'Staggered-T-Junction'), ('Rotary-Or-Roundabout', 'Rotary-Or-Roundabout')], max_length=50, null=True)),
                ('number_of_lanes', models.CharField(blank=True, max_length=100, null=True)),
                ('central_marking', models.CharField(blank=True, choices=[('None', 'None'), ('Broken-Single', 'Broken-Single'), ('Broken-Double', 'Broken-Double'), ('Continuous-Single', 'Continuous-Single'), ('Continuous-Double', 'Continuous-Double')], max_length=50, null=True)),
                ('footpath_info', models.TextField(blank=True, null=True)),
                ('one_way_two_way', models.CharField(max_length=10)),
                ('width_each_side', models.FloatField(blank=True, null=True)),
                ('pictures_near_side', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('pictures_far_side', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('traffic_lights', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('traffic_lights_working', models.CharField(blank=True, max_length=15, null=True)),
                ('num_traffic_lights', models.IntegerField(blank=True, null=True)),
                ('traffic_lights_pictures', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('zebra_crossings', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('zebra_crossings_latitude', models.CharField(max_length=100)),
                ('zebra_crossings_longitude', models.CharField(max_length=100)),
                ('num_zebra_crossings', models.IntegerField(blank=True, null=True)),
                ('zebra_width', models.FloatField(blank=True, null=True)),
                ('foot_over_bridge', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('num_foot_over_bridges', models.IntegerField(blank=True, null=True)),
                ('foot_over_bridge_picture', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('power_source', models.CharField(blank=True, max_length=50, null=True)),
                ('power_source_picture', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('electric_poles_picture', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('on_street_vehicle_parking', models.CharField(max_length=3)),
                ('both_sides_or_one_side', models.CharField(choices=[('Both', 'Both'), ('One', 'One')], max_length=4)),
                ('viable_installation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('reason', models.TextField(blank=True, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.school')),
            ],
        ),
        migrations.CreateModel(
            name='RoadwayFacilityNear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carriage_width', models.FloatField()),
                ('carriage_direction', models.CharField(choices=[('North-South', 'North-South'), ('East-West', 'East-West'), ('North', 'North'), ('South', 'South'), ('East', 'East'), ('West', 'West')], max_length=20)),
                ('divided', models.CharField(choices=[('Undivided', 'Undivided'), ('Central Refuge', 'Central Refuge'), ('Barrier', 'Barrier')], max_length=20)),
                ('intersection_type', models.CharField(blank=True, choices=[('No-Intersection', 'No-Intersection'), ('T-Junction', 'T-Junction'), ('4-Legged-Intersection', '4-Legged-Intersection'), ('Y-Junction', 'Y-Junction'), ('Staggered-T-Junction', 'Staggered-T-Junction'), ('Rotary-Or-Roundabout', 'Rotary-Or-Roundabout')], max_length=50, null=True)),
                ('number_of_lanes', models.CharField(blank=True, max_length=100, null=True)),
                ('central_marking', models.CharField(blank=True, choices=[('None', 'None'), ('Broken-Single', 'Broken-Single'), ('Broken-Double', 'Broken-Double'), ('Continuous-Single', 'Continuous-Single'), ('Continuous-Double', 'Continuous-Double')], max_length=50, null=True)),
                ('footpath_info', models.TextField(blank=True, null=True)),
                ('one_way_two_way', models.CharField(max_length=10)),
                ('width_each_side', models.FloatField(blank=True, null=True)),
                ('pictures_near_side', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('pictures_far_side', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('traffic_lights', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('traffic_lights_working', models.CharField(blank=True, max_length=15, null=True)),
                ('num_traffic_lights', models.IntegerField(blank=True, null=True)),
                ('traffic_lights_pictures', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('zebra_crossings', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('zebra_crossings_latitude', models.CharField(max_length=100)),
                ('zebra_crossings_longitude', models.CharField(max_length=100)),
                ('num_zebra_crossings', models.IntegerField(blank=True, null=True)),
                ('zebra_width', models.FloatField(blank=True, null=True)),
                ('foot_over_bridge', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('num_foot_over_bridges', models.IntegerField(blank=True, null=True)),
                ('foot_over_bridge_picture', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('power_source', models.CharField(blank=True, max_length=50, null=True)),
                ('power_source_picture', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('electric_poles_picture', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('on_street_vehicle_parking', models.CharField(max_length=3)),
                ('both_sides_or_one_side', models.CharField(choices=[('Both', 'Both'), ('One', 'One')], max_length=4)),
                ('viable_installation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('reason', models.TextField(blank=True, null=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.school')),
            ],
        ),
        migrations.RemoveField(
            model_name='roadwayfacility',
            name='school',
        ),
        migrations.DeleteModel(
            name='RoadwayInfo',
        ),
        migrations.DeleteModel(
            name='RoadwayFacility',
        ),
    ]
