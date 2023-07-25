# Generated by Django 4.2.2 on 2023-07-06 13:14

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0003_alter_homepage_options_homepage_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_text',
            field=wagtail.fields.RichTextField(default='Test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='banner',
            field=models.CharField(default='test text', help_text='catch phrase', max_length=100, verbose_name='Banners'),
            preserve_default=False,
        ),
    ]
