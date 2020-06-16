from modeltranslation.translator import TranslationOptions, register
from .models import Product, Category, Services, Billboard, AboutUs


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'subtitle', 'category')
    required_languages = ('en', 'zh-tw')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category',)
    required_languages = ('en', 'zh-tw')

@register(Billboard)
class SiteConfigTranslationOptions(TranslationOptions):
    fields = ('headline', 'subtitle',)
    required_languages = ('en', 'zh-tw')

@register(AboutUs)
class SiteConfigTranslationOptions(TranslationOptions):
    fields = ('maintext',)
    required_languages = ('en', 'zh-tw')

@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('headline', 'text',)
    required_languages = ('en', 'zh-tw')
