# tradingapp/models.py
from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser


class SiteSettings(models.Model):
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)

    # Banner image (new)
    home_banner = models.ImageField(upload_to="banners/", blank=True, null=True)

    # New fields for knowledge section
    knowledge_title = models.CharField(max_length=200, )
    knowledge_highlight = models.CharField(max_length=200, )
    knowledge_description = models.TextField()
    knowledge_blog_name = models.CharField(max_length=50,)

    def __str__(self):
        return "Site Settings"
#next 4 tabs#
class Category(models.Model):
    
    name = models.CharField(max_length=100, unique=True)  # Stocks, Mutual Funds, etc.
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    read_time = models.CharField(max_length=50, help_text="e.g. '5 Mins Read'")
    date = models.DateField()
    image = models.ImageField(upload_to="posts/")
    
    def __str__(self):
        return self.title
    
class FooterSettings(models.Model):
    logo_text = models.CharField(max_length=100, default="ITRACO")
    newsletter_text = models.TextField(blank=True, null=True, help_text="Small description under newsletter")
    
    facebook_image = models.ImageField(upload_to="footer/", blank=True, null=True)
    twitter_image = models.ImageField(upload_to="footer/", blank=True, null=True)
    instagram_image = models.ImageField(upload_to="footer/", blank=True, null=True)

    def __str__(self):
        return "Footer Settings"

class FooterMenu(models.Model):
    SECTION_CHOICES = [
        ("main", "Main"),
        ("info", "Information"),
        ("resources", "Resources"),
    ]
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    title = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_section_display()} - {self.title}"
    
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

from django.db import models

class HomeBanner(models.Model):
    # Background & Right side image
    background_image = models.ImageField(upload_to="banners/", blank=True, null=True)
    right_image = models.ImageField(upload_to="banners/", blank=True, null=True)

    # Text Content
    subtitle = models.CharField(max_length=200, default="Keep Your Money Safe !!!!")
    title = models.CharField(max_length=300, default="Build Confidence With Every Single Trade.")
    highlight = models.CharField(max_length=300, default="Invest for Your Future")
    description = models.TextField(default="Your Trading Journey Started Here....")

    # Avatars
    user1 = models.ImageField(upload_to="avatars/", blank=True, null=True)
    user2 = models.ImageField(upload_to="avatars/", blank=True, null=True)
    user3 = models.ImageField(upload_to="avatars/", blank=True, null=True)
    user4 = models.ImageField(upload_to="avatars/", blank=True, null=True)
    user5 = models.ImageField(upload_to="avatars/", blank=True, null=True)

    # Stats
    users_count = models.CharField(max_length=50, default="500+")
    users_label = models.CharField(max_length=100, default="Realtime Users")

    # Button
    button_text = models.CharField(max_length=100, default="Start Now")
    button_link = models.URLField(default="#")

    def __str__(self):
        return "Home Banner"

class SectionBackground(models.Model):
    background_image = models.ImageField(upload_to="section_backgrounds/", blank=True, null=True)

    def __str__(self):
        return f"Background {self.id}"

class HomeSection(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    subtitle = models.TextField(blank=True, null=True)
    highlight_text = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    right_image = models.ImageField(upload_to="home_section/", blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Home Section"
    
class Feature(models.Model):
    number = models.CharField(max_length=5, help_text="e.g. 01, 02, 03")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    link_text = models.CharField(max_length=100, blank=True, null=True, default="Learn More")
    link_url = models.URLField(blank=True, null=True)
    highlight = models.BooleanField(default=False, help_text="Highlight this column in green?")

    def __str__(self):
        return f"{self.number}. {self.title}"
class HowItWorksSection(models.Model):
    background = models.ImageField(upload_to="howitworks_bg/", help_text="Background image for How it Works section")

    def __str__(self):
        return "How It Works Section Background"


class HowItWorks(models.Model):
    title = models.CharField(max_length=200)  # e.g. Apply
    description = models.TextField()  # e.g. Join thousands of traders...
    position = models.PositiveIntegerField(help_text="Order of step (1,2,3,4)")
    image = models.ImageField(upload_to="howitworks/", blank=True, null=True, help_text="Optional icon image")

    def __str__(self):
        return f"Step {self.position}: {self.title}"

    class Meta:
        ordering = ["position"]

class DashboardBackground(models.Model):
    background_image = models.ImageField(upload_to="dashboard_backgrounds/", blank=True, null=True)

    def __str__(self):
        return f"Background {self.id}"
    
class CommunitySection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class CommunityImage(models.Model):
    section = models.ForeignKey(CommunitySection, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="community/")
    order = models.PositiveIntegerField(default=1, help_text="Order of image display (1,2,3,...)")

    def __str__(self):
        return f"Image {self.order} for {self.section.title}"

    class Meta:
        ordering = ["order"]


class AboutSection(models.Model):
    title = models.CharField(max_length=200, default="About TRACO")
    background_image = models.ImageField(upload_to="about/", blank=True, null=True)

    def __str__(self):
        return self.title
    
class AboutPage(models.Model):
    title = models.CharField(max_length=200 )
    intro = models.TextField(max_length=300)
    intro_secondary = models.TextField(max_length=200 )
    
    mission_title = models.CharField(max_length=200 )
    mission_text = models.TextField(max_length=200 )

    vision_title = models.CharField(max_length=200 )
    vision_text = models.TextField(max_length=200 )

    image = models.ImageField(upload_to='about/', help_text="Team image")

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Page Content"
    
class AboutFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='about_icons/')  # PNG/SVG images

    class Meta:
        verbose_name = "About Feature"
        verbose_name_plural = "About Features"

    def __str__(self):
        return self.title
    

class PartnerCity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PartnerRequest(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.ForeignKey(PartnerCity, on_delete=models.SET_NULL, null=True, blank=True)
    pincode = models.CharField(max_length=10)
    otp = models.CharField(max_length=6, blank=True, null=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
    

class PartnerPageContent(models.Model):
    image = models.ImageField(upload_to="partners/")
    heading = models.CharField(max_length=255, default="Welcome to the First Step of Becoming a TRACO Partner")
    contact_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Partner Page Content"
    
class PartnerBenefit(models.Model):
    ICON_POSITIONS = [
        ("left", "Left"),
        ("right", "Right"),
    ]

    title = models.CharField(max_length=100)   # Example: Technology, Research
    description = models.TextField()           # Example: Full description text
    icon = models.ImageField(upload_to="partner/icons/")  # Upload icon from admin
    order = models.PositiveIntegerField(default=0)        # To control display order
    highlighted = models.BooleanField(default=True)       # For green title

    def __str__(self):
        return self.title
    

#loginform



class AuthPageContent(models.Model):
    page_type = models.CharField(
        max_length=20,
        choices=[("login", "Login Page"), ("register", "Register Page")]
    )
    heading = models.CharField(max_length=200)
    subheading = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="auth_pages/", blank=True, null=True)

    def __str__(self):
        return f"{self.page_type} - {self.heading}"