from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page,Orderable
from wagtail.admin.panels import FieldPanel,PageChooserPanel,InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from streams import blocks

class HomePageCarrousel(Orderable):
    page = ParentalKey("home.HomePage", related_name = "carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = False,
        on_delete= models.SET_NULL,
        related_name = "+"
    )
    panels = [
        PageChooserPanel("carousel_image")
    ]

class HomePage(Page):
    """Home Page Model"""
    templates = "home/home_page.html"
    max_count=1
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["blog.BlogListingPage", "flex.Flexpage",]

    banner = models.CharField(
        "Banners",
        blank=False,
        null=False,
        max_length=100,
        help_text="catch phrase", 
        )
    
    
    banner_text = RichTextField(features = ["bold","italics"] )

    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null = True,
        blank = False,
        on_delete= models.SET_NULL,
        related_name = "+"
    )

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null = True,
        blank = True,
        on_delete= models.SET_NULL,
        related_name = "+"
    )

    content = StreamField ([
        ("CTA", blocks.CTA())
    ],
    use_json_field=True, null=True)


    content_panels=Page.content_panels+[
        MultiFieldPanel([
            FieldPanel("banner"), 
            FieldPanel("banner_text"), 
            FieldPanel("banner_image"), 
            PageChooserPanel("banner_cta"),
             
            ], heading = 'Banner section'),

        MultiFieldPanel([
            InlinePanel("carousel_images", max_num = 4, min_num=1, label = "images")
        ], heading = 'Carousel Images'),

        FieldPanel("content"),
       ]

    class Meta:
        verbose_name= "Home Page"
        verbose_name_plural ="Home Pages"
