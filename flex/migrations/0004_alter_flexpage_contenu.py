# Generated by Django 4.2.2 on 2023-07-12 08:25

from django.db import migrations
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0003_alter_flexpage_contenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='contenu',
            field=wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='entrez un titre', required=True)), ('text', wagtail.blocks.TextBlock(help_text='entrez un texte', required=True))])), ('full_richtext', streams.blocks.RichText()), ('card_service', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='entrez un titre', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('titre', wagtail.blocks.CharBlock(max_length='100', required=True)), ('text', wagtail.blocks.CharBlock(max_length='400', required=True)), ('date', wagtail.blocks.DateBlock(required=True)), ('boutonI', wagtail.blocks.PageChooserBlock(required=False)), ('boutonE', wagtail.blocks.URLBlock(required=False))])))])), ('CTA', wagtail.blocks.StructBlock([('titre', wagtail.blocks.CharBlock(max_length='100', required=True)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('boutonIn', wagtail.blocks.PageChooserBlock(required=False)), ('boutonUrl', wagtail.blocks.URLBlock(required=False)), ('boutonText', wagtail.blocks.CharBlock(max_length='400', required=True))]))], null=True, use_json_field=True),
        ),
    ]
