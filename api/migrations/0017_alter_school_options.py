# Generated by Django 5.1.1 on 2024-10-02 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_finalizationform_school'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['school_name'], 'verbose_name': 'School', 'verbose_name_plural': 'Schools'},
        ),
    ]
