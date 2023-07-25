from django.db import models
from wagtail import blocks
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from streams import blocks



class BlogListingPage(Page):

    template = "blog/blog_listing_page.html"
    custom_title = models.CharField(
        max_length = 100,
        blank = False,
        null = False,
        help_text = "Overwrites the default title",)

    content_panels = Page.content_panels + [
    FieldPanel("custom_title"),]

    subpage_types = ["blog.BlogDetailPage",]

    def get_context(self, request,*args, **kwargs):
        """Adding custom stuff to our context"""
        context = super().get_context(request,*args, **kwargs)
        context["posts"]= BlogDetailPage.objects.live().public()
        return context


class BlogDetailPage(Page):
    custom_title = models.CharField(
        max_length =  100,
        blank = False,
        null = True,
        help_text = "Overwrites the default title",
    )
    blog_image = models.ForeignKey(
         "wagtailimages.Image",
         blank = False,
         null = True,
         related_name= "+",
         on_delete=models.SET_NULL,  
     )
    contenu = StreamField([
        ("title_and_text", blocks.TitleAndText()),
        ("full_richtext", blocks.RichText()),
        ("card_service", blocks.Cards()),
        ("CTA", blocks.CTA())
    ],
    use_json_field=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("blog_image"),
        FieldPanel("contenu"),
    ]

     


# Create your models here.
