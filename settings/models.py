from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify


class websiteSetting(models.Model):
    name = models.TextField(default='Application Name')
    logo_dark = models.ImageField(upload_to='app_config/')
    logo = models.ImageField(upload_to='app_config/')
    logo_width = models.IntegerField(blank=True, null=True)
    invoice_logo = models.ImageField(upload_to='app_config', blank=True, null=True)
    invoice_logo_width = models.IntegerField(blank=True, null=True)
    favicon = models.ImageField(upload_to='app_config/')
    
    author = models.CharField(max_length=200, default='Author Name', blank=True, null=True)
    email_address = models.TextField(default='support@synclo.io', blank=True, null=True)
    phone_or_whatsapp = models.CharField(max_length=20, default='+918143024666', blank=True, null=True)
    price_ragne = models.CharField(max_length=50, default='60$ to 7000$', blank=True, null=True)
    country = models.CharField(max_length=300, default='Your Country', blank=True, null=True)
    address = models.CharField(max_length=700, default='Your Address', blank=True, null=True)
    state = models.CharField(max_length=200, default='Your State', blank=True, null=True)
    Zip = models.IntegerField(default=12345)
    
    analytics_code = models.CharField(max_length=300, blank=True, null=True, default="GA_MEASUREMENT_ID")
    facebook_pixel_code = models.TextField(blank=True, null=True)
    facebook_chat_code = models.TextField(blank=True, null=True)
    whatsapp_is_active = models.BooleanField(default=True)
    messenger_is_active = models.BooleanField(default=True)
    default_menu_is_active = models.BooleanField(default=True)
    
    currency_name = models.CharField(max_length=100, default='USD')
    currency_symbol = models.CharField(max_length=150, default='$')
    
    twilio_sid = models.TextField(blank=True, null=True)
    twilio_auth_token = models.TextField(blank=True, null=True)
    twilio_message_service_sid = models.TextField(blank=True, null=True)
    
    openai_api = models.CharField(max_length=1000, blank=True, null=True)
    max_token = models.IntegerField(default=150, blank=True, null=True)
    is_enabled_for_user = models.BooleanField(default=False)
    
    is_purchasing_enable = models.BooleanField(default=True)
    is_auto_invoice_enable = models.BooleanField(default=True)
    
    custom_css = models.TextField(blank=True, null=True)
    custom_js = models.TextField(blank=True, null=True)
    
class SeoSetting(models.Model):
    meta_title = models.CharField(max_length=500, blank=True, null=True)
    tag_line = models.CharField(max_length=600, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    seo_keywords = models.TextField(default='software,application,marketer,developer', blank=True, null=True)
    meta_image = models.ImageField(upload_to='app_config/', blank=True, null=True)

    def __str__(self):
        return 'SEO Setting Configs'

class Menu(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=500)
    order = models.IntegerField()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class HeaderFooter(models.Model):
    
    footer_col1_subtitle = models.CharField(max_length=300)
    footer_col1_title = models.CharField(max_length=300)
    footer_col1_button = models.CharField(max_length=300)
    footer_col1_button_url = models.CharField(max_length=500)
    
    facebook = models.CharField(max_length=300, blank=True, null=True, default="https://facebook.com")
    instagram = models.CharField(max_length=300, blank=True, null=True, default="https://instagram.com")
    twitter = models.CharField(max_length=300, blank=True, null=True, default="https://twitter.com")
    linkedin = models.CharField(max_length=300, blank=True, null=True, default="https://linkedin.com")
    youtube = models.CharField(max_length=300, blank=True, null=True, default="https://youtube.com")
    pinterest = models.CharField(max_length=300, blank=True, null=True, default="https://pinterest.com")
    
    footer_col2_title1 = models.CharField(max_length=300)
    footer_col2_description1 = RichTextField()
    
    footer_col2_title2 = models.CharField(max_length=300)
    footer_col2_description2 = RichTextField()
    
    footer_copyright = models.CharField(max_length=500)
    
class paymentMethod(models.Model):
    # SSL Commerze
    ssl_commerze_store_id = models.CharField(max_length=255, blank=True, null=True)
    ssl_commerze_store_pass = models.CharField(max_length=255, blank=True, null=True)
    ssl_commerze_is_sandbox = models.BooleanField(default=False)
    ssl_commerze_is_active = models.BooleanField(default=False)
    
    # PayPal
    paypal_client_id = models.TextField(blank=True, null=True)
    paypal_client_secret = models.TextField(blank=True, null=True)
    paypal_is_sandbox = models.BooleanField(default=False)
    paypal_is_active = models.BooleanField(default=False)
    
    # Stripe
    stripe_publish_key = models.TextField(blank=True, null=True)
    stripe_secret_key = models.TextField(blank=True, null=True)
    stripe_is_sandbox = models.BooleanField(default=False)
    stripe_is_active = models.BooleanField(default=False)
    
    # Stripe
    instamojo_api_key = models.TextField(blank=True, null=True)
    instamojo_auth_token = models.TextField(blank=True, null=True)
    instamojo_is_sandbox = models.BooleanField(default=False)
    instamojo_is_active = models.BooleanField(default=False)
    
    # Razorpay
    razorpay_api_key = models.TextField(blank=True, null=True)
    razorpay_api_secret = models.TextField(blank=True, null=True)
    razorpay_is_active = models.BooleanField(default=False)
    
    # Offline Payment
    offline_payment_instruction = RichTextField()
    offline_payment_is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return 'Payment Methods'
