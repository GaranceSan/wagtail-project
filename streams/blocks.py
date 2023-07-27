from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndText(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="entrez un titre")
    text= blocks.TextBlock(required=True, help_text="entrez un texte")

    class Meta:
        template = "streams/title_and_text.html"
        icon = "edit"
        label = "Title & Text"

class RichText(blocks.RichTextBlock):
    class Meta: 
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"

class Card(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    titre =  blocks.CharBlock(required=True, max_length="100")
    text =  blocks.CharBlock(required=True, max_length="400")
    date = blocks.DateBlock(required=True)
    boutonI =  blocks.PageChooserBlock(required=False)
    boutonE = blocks.URLBlock(required=False)


class Cards(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="entrez un titre")
    cards = blocks.ListBlock(Card())
        

    class Meta: 
        template = "streams/card_service.html"
        icon = "placeholder"
        label = "Cards"

class CTA(blocks.StructBlock):
    titre =  blocks.CharBlock(required=True, max_length="100")
    text = blocks.RichTextBlock(required = True, features = ["bold", "italic"])
    boutonIn =  blocks.PageChooserBlock(required=False)
    boutonUrl = blocks.URLBlock(required=False)
    boutonText = blocks.CharBlock(required=True, max_length="400")

    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"

class LinkStructValue(blocks.StructValue):
    def url(self):
        button1= self.get("button_page_url")
        button2= self.get("button_outside_url")
        if button1:
            return button1.url
        elif button2:
            return button2
        return None

class ButtonBlock(blocks.StructBlock):
    
    button_page_url= blocks.PageChooserBlock(required=False)
    button_outside_url= blocks.URLBlock(required=False)

    class Meta:
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Single button"
        value_class= LinkStructValue