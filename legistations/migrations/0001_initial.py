# Generated by Django 3.2 on 2022-07-08 14:31

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegislationListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='LegislationPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('description', wagtail.fields.RichTextField(blank=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('countries', django_countries.fields.CountryField(max_length=746, multiple=True)),
                ('date_issued', models.DateField(blank=True)),
                ('date_into_practice', models.DateField(blank=True)),
                ('external_page', models.URLField(blank=True)),
                ('button_text', models.CharField(blank=True, max_length=50)),
                ('internal_page', models.ForeignKey(blank=True, help_text='Select an internal wagtail page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('legislation_image', models.ForeignKey(help_text='This image will be used on the service Listing page and will be cropped to 570px by 370px on this page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
