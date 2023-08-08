from django.db import models
from django import forms
from wagtail import blocks
from wagtail.models import Page,Orderable
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel
from wagtail.fields import StreamField
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.snippets.models import register_snippet
from streams import blocks

class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        verbose_name= "slug",
        allow_unicode= True,
        max_length= 255
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug")
    ]

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__ (self) :
        return self.name

register_snippet(Categories)




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
        all_posts = BlogDetailPage.objects.live().public().order_by("-first_published_at")
     
        paginator= Paginator(all_posts,1)
        page= request.GET.get("page")
        try: 
            posts=paginator.page(page)
        except PageNotAnInteger:
            posts=paginator.page(1)
        except EmptyPage:
            posts=paginator.page(paginator.num_pages)

        context["posts"]= posts

        context["categories"]=Categories.objects.all()
        return context


class BlogDetailPage(Page):
    custom_title = models.CharField(
        max_length =  100,
        blank = True,
        null = True,
        help_text = "Overwrites the default title",
    )
    blog_image = models.ForeignKey(
         "wagtailimages.Image",
         blank = True,
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

    categories = ParentalManyToManyField("blog.Categories", blank=True)

class ArticleBlogPage(BlogDetailPage):
    template = "blog/article_blog_page.html"

    subtitle = models.CharField(max_length=100,blank=True, null=True)

    
    intro_image = models.ForeignKey("wagtailimages.Image", blank=True, null=True, on_delete=models.SET_NULL)


    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("blog_image"),
        FieldPanel("subtitle"),
        FieldPanel("intro_image"),
        FieldPanel("contenu"),
        MultiFieldPanel([
            InlinePanel("blog_authors", label="Authors", min_num=1)],
            heading="Author(s)"),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget = forms.CheckboxSelectMultiple)
            ], heading = "categories"
        )
        ]
    

    

     


# Create your models here.
