# Generated by Django 4.0.6 on 2022-07-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_background_image_homepage_button_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='lead_text',
            field=models.CharField(blank=True, help_text='Subheader text under the banner title', max_length=500),
        ),
    ]
