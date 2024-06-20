# Generated by Django 5.0.3 on 2024-03-13 15:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            sql="DROP TABLE IF EXISTS `settings_headerfooter`;",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.RunSQL(
            sql="DROP TABLE IF EXISTS `settings_menu`;",
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.CreateModel(
            name='HeaderFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_col1_subtitle', models.TextField()),
                ('footer_col1_title', models.TextField()),
                ('footer_col1_button', models.TextField()),
                ('footer_col1_button_url', models.TextField()),
                ('facebook', models.TextField(blank=True, default='https://facebook.com', null=True)),
                ('instagram', models.TextField(blank=True, default='https://instagram.com', null=True)),
                ('twitter', models.TextField(blank=True, default='https://twitter.com', null=True)),
                ('linkedin', models.TextField(blank=True, default='https://linkedin.com', null=True)),
                ('youtube', models.TextField(blank=True, default='https://youtube.com', null=True)),
                ('pinterest', models.TextField(blank=True, default='https://pinterest.com', null=True)),
                ('footer_col2_title1', models.TextField()),
                ('footer_col2_description1', ckeditor.fields.RichTextField()),
                ('footer_col2_title2', models.TextField()),
                ('footer_col2_description2', ckeditor.fields.RichTextField()),
                ('footer_copyright', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('url', models.TextField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='paymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssl_commerze_store_id', models.TextField(blank=True, null=True)),
                ('ssl_commerze_store_pass', models.TextField(blank=True, null=True)),
                ('ssl_commerze_is_sandbox', models.BooleanField(default=False)),
                ('ssl_commerze_is_active', models.BooleanField(default=False)),
                ('paypal_client_id', models.TextField(blank=True, null=True)),
                ('paypal_client_secret', models.TextField(blank=True, null=True)),
                ('paypal_is_sandbox', models.BooleanField(default=False)),
                ('paypal_is_active', models.BooleanField(default=False)),
                ('stripe_publish_key', models.TextField(blank=True, null=True)),
                ('stripe_secret_key', models.TextField(blank=True, null=True)),
                ('stripe_is_sandbox', models.BooleanField(default=False)),
                ('stripe_is_active', models.BooleanField(default=False)),
                ('instamojo_api_key', models.TextField(blank=True, null=True)),
                ('instamojo_auth_token', models.TextField(blank=True, null=True)),
                ('instamojo_is_sandbox', models.BooleanField(default=False)),
                ('instamojo_is_active', models.BooleanField(default=False)),
                ('razorpay_api_key', models.TextField(blank=True, null=True)),
                ('razorpay_api_secret', models.TextField(blank=True, null=True)),
                ('razorpay_is_active', models.BooleanField(default=False)),
                ('offline_payment_instruction', ckeditor.fields.RichTextField()),
                ('offline_payment_is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SeoSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.TextField(blank=True, null=True)),
                ('tag_line', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('seo_keywords', models.TextField(blank=True, default='software,application,marketer,developer', null=True)),
                ('meta_image', models.ImageField(blank=True, null=True, upload_to='app_config/')),
            ],
        ),
        migrations.CreateModel(
            name='websiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Application Name', max_length=500)),
                ('logo_dark', models.ImageField(upload_to='app_config/')),
                ('logo', models.ImageField(upload_to='app_config/')),
                ('logo_width', models.IntegerField(blank=True, null=True)),
                ('invoice_logo', models.ImageField(blank=True, null=True, upload_to='app_config')),
                ('invoice_logo_width', models.IntegerField(blank=True, null=True)),
                ('favicon', models.ImageField(upload_to='app_config/')),
                ('author', models.CharField(blank=True, default='Author Name', max_length=200, null=True)),
                ('email_address', models.EmailField(blank=True, default='test@gmail.com', max_length=500, null=True)),
                ('phone_or_whatsapp', models.CharField(blank=True, default='+918143024666', max_length=20, null=True)),
                ('price_ragne', models.CharField(blank=True, default='60$ to 7000$', max_length=50, null=True)),
                ('country', models.CharField(blank=True, default='Your Country', max_length=300, null=True)),
                ('address', models.CharField(blank=True, default='Your Address', max_length=700, null=True)),
                ('state', models.CharField(blank=True, default='Your State', max_length=200, null=True)),
                ('Zip', models.IntegerField(default=12345)),
                ('analytics_code', models.CharField(blank=True, default='GA_MEASUREMENT_ID', max_length=300, null=True)),
                ('facebook_pixel_code', models.TextField(blank=True, null=True)),
                ('facebook_chat_code', models.TextField(blank=True, null=True)),
                ('whatsapp_is_active', models.BooleanField(default=True)),
                ('messenger_is_active', models.BooleanField(default=True)),
                ('default_menu_is_active', models.BooleanField(default=True)),
                ('currency_name', models.CharField(default='USD', max_length=100)),
                ('currency_symbol', models.CharField(default='$', max_length=150)),
                ('twilio_sid', models.TextField(blank=True, null=True)),
                ('twilio_auth_token', models.TextField(blank=True, null=True)),
                ('twilio_from_number', models.CharField(blank=True, max_length=15, null=True)),
                ('openai_api', models.TextField(blank=True, null=True)),
                ('max_token', models.IntegerField(blank=True, default=150, null=True)),
                ('is_enabled_for_user', models.BooleanField(default=False)),
                ('is_purchasing_enable', models.BooleanField(default=True)),
                ('is_auto_invoice_enable', models.BooleanField(default=True)),
                ('custom_css', models.TextField(blank=True, null=True)),
                ('custom_js', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
