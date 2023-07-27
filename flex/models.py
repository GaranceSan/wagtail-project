from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField


from streams import blocks

class Flexpage(Page):
    template = "flex/flex.html"
    soustitre = models.CharField(max_length=100, blank=True, null=True)
    contenu = StreamField([
        ("title_and_text", blocks.TitleAndText()),
        ("full_richtext", blocks.RichText()),
        ("card_service", blocks.Cards()),
        ("CTA", blocks.CTA()),
        ("button_block", blocks.ButtonBlock()),
    ],
    use_json_field=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("soustitre"), 
        FieldPanel("contenu"),
    
    ] 

    class Meta: 
        verbose_name= "Flex Page"
        verbose_name_plural = "Flex Pages"