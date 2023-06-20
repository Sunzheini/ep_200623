# Generated by Django 4.2.2 on 2023-06-20 08:18

from django.db import migrations, models
import ep_200623.expenses_tracker.models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_tracker', '0004_alter_profile_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[ep_200623.expenses_tracker.models.max_size_validator]),
        ),
    ]