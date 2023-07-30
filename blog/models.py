from django.db import models
from wagtail import blocks
from wagtail.models import Page,Orderable
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel
from wagtail.fields import StreamField
from wagtail.snippets.models import register_snippet
from streams import blocks

class BlogAuthorsOrderable(Orderable):
    page = ParentalKey("blog.BlogDetailPage", related_name="blog_authors")
    author = models.ForeignKey (
        "blog.AuthorsSnippets",
        on_delete = models.CASCADE,
    )

class AuthorsSnippets(models.Model):

    name = models.CharField(        
        max_length = 100,
        blank = False,
        null = False,)
    
    intro = models.TextField(
        max_length = 500,
        blank = False,
        null = True,
    )
    image = models.ForeignKey(
         "wagtailimages.Image",
         blank = False,
         null = True,
         related_name= "+",
         on_delete=models.SET_NULL,  
     )

    panels = [
        MultiFieldPanel(
        [
            FieldPanel("name"),
            FieldPanel("intro"),
         ],
         heading="Name and Intro"),
        MultiFieldPanel(
         [ 
             FieldPanel("image")
         ],
         heading="Pic"
    )]

    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name = "blog author"
        verbose_name_plural = "blog authors"

register_snippet(AuthorsSnippets)



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
         on_delete=models.SET_NULL,)
    
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
        MultiFieldPanel([
            InlinePanel("blog_authors", label="Authors", min_num=1)],
            heading="Author(s)")
        ]
    

     


# Create your models here.
