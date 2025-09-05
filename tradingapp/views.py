from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (
    SiteSettings, Category, Post,
    FooterSettings, FooterMenu,
    HomeBanner, SectionBackground, HomeSection,
    Feature, HowItWorks, HowItWorksSection,
    DashboardBackground, CommunitySection
)
from .forms import SubscriberForm
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  login
from .models import AboutSection,AboutPage,AboutFeature
from django.http import JsonResponse
import random
from django.contrib import messages
from .models import PartnerRequest, PartnerPageContent,PartnerBenefit
from .forms import PartnerRequestForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
OTP_STORAGE = {}


def blogs(request):
    settings = SiteSettings.objects.first()
    categories = Category.objects.all()
    current_category = categories.first()
    posts = Post.objects.filter(category=current_category).order_by("-date")[:3]

    footer_settings = FooterSettings.objects.first()
    footer_menus = {
        "main": FooterMenu.objects.filter(section="main"),
        "info": FooterMenu.objects.filter(section="info"),
        "resources": FooterMenu.objects.filter(section="resources"),
    }

    # Handle subscription
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for subscribing!")
            return redirect(request.path)
    else:
        form = SubscriberForm()

    context = {
        "settings": settings,
        "categories": categories,
        "current_category": current_category,
        "posts": posts,
        "footer_settings": footer_settings,
        "footer_menus": footer_menus,
        "subscriber_form": form,
    }
    return render(request, "tradingapp/blogs.html", context)


def home(request):
    settings = SiteSettings.objects.first()  # <-- add this

    banner = HomeBanner.objects.first()
    section_bg = SectionBackground.objects.first()
    section = HomeSection.objects.first()
    features = Feature.objects.all().order_by("number")
    how_it_works = HowItWorks.objects.all()
    how_section = HowItWorksSection.objects.first()
    dashboard_bg = DashboardBackground.objects.first()

    # Community Section
    community = CommunitySection.objects.first()
    community_images = community.images.all() if community else []

    # Footer
    footer_settings = FooterSettings.objects.first()
    footer_menus = {
        "main": FooterMenu.objects.filter(section="main"),
        "info": FooterMenu.objects.filter(section="info"),
        "resources": FooterMenu.objects.filter(section="resources"),
    }

    # Subscription form
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for subscribing!")
            return redirect(request.path)
    else:
        form = SubscriberForm()

    context = {
        "settings": settings,  # <-- pass this to template
        "banner": banner,
        "avatars": [],
        "section_bg": section_bg,
        "section": section,
        "features": features,
        "how_it_works": how_it_works,
        "how_section": how_section,
        "dashboard_bg": dashboard_bg,
        "community": community,
        "community_images": community_images,
        "footer_settings": footer_settings,
        "footer_menus": footer_menus,
        "subscriber_form": form,
    }
    return render(request, "tradingapp/home.html", context)

#About page
def about(request):
    settings = SiteSettings.objects.first()  
    about_section = AboutSection.objects.first()
    about_page = AboutPage.objects.first()
    features = AboutFeature.objects.all()

        # Footer data (same as blogs)
    footer_settings = FooterSettings.objects.first()
    footer_menus = {
        "main": FooterMenu.objects.filter(section="main"),
        "info": FooterMenu.objects.filter(section="info"),
        "resources": FooterMenu.objects.filter(section="resources"),
    }

    # Handle subscription form
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for subscribing!")
            return redirect(request.path)
    else:
        form = SubscriberForm()

    return render(request, 'tradingapp/about.html', {
        "settings": settings,  
        "about_section": about_section,
        "about_page": about_page,
        "features": features,
        "footer_settings": footer_settings,
        "footer_menus": footer_menus,
        "subscriber_form": form,
    })

#partnerpage



def verify_otp(request, partner_id):
    try:
        partner = PartnerRequest.objects.get(id=partner_id)
    except PartnerRequest.DoesNotExist:
        messages.error(request, "Invalid request.")
        return redirect("become_partner")

    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        if entered_otp == partner.otp:
            partner.verified = True
            partner.save()
            messages.success(request, "Your account has been verified successfully!")
            return redirect("become_partner")
        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, "tradingapp/verify_otp.html", {"partner": partner})

def become_partner(request):
    settings = SiteSettings.objects.first()
    page_content = PartnerPageContent.objects.first()
    benefits = PartnerBenefit.objects.all().order_by("order")

    partner_form = PartnerRequestForm()
    subscriber_form = SubscriberForm()

    if request.method == "POST":
        if "partner_submit" in request.POST:
            partner_form = PartnerRequestForm(request.POST)
            if partner_form.is_valid():
                partner = partner_form.save(commit=False)
                partner.otp = str(random.randint(100000, 999999))
                partner.save()
                print(f"OTP for {partner.phone}: {partner.otp}")
                messages.success(request, "OTP sent to your mobile/email")
                return redirect("verify_otp", partner_id=partner.id)

        elif "subscriber_submit" in request.POST:
            subscriber_form = SubscriberForm(request.POST)
            if subscriber_form.is_valid():
                subscriber_form.save()
                messages.success(request, "Thanks for subscribing!")
                return redirect(request.path)

    # Footer
    footer_settings = FooterSettings.objects.first()
    footer_menus = {
        "main": FooterMenu.objects.filter(section="main"),
        "info": FooterMenu.objects.filter(section="info"),
        "resources": FooterMenu.objects.filter(section="resources"),
    }

    return render(request, "tradingapp/become_partner.html", {
        "settings": settings,  
        "partner_form": partner_form,
        "subscriber_form": subscriber_form,
        "page_content": page_content,
        "benefits": benefits,
        "footer_settings": footer_settings,
        "footer_menus": footer_menus,
    })


# Register
def signup_view(request):
    settings = SiteSettings.objects.first()
    signup_form = SignUpForm()
    subscriber_form = SubscriberForm()
    
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.email = signup_form.cleaned_data.get("email")
            user.first_name = signup_form.cleaned_data.get("name")
            user.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("home")
        else:
            messages.error(request, "Please correct the errors below.")
    
    # Footer
    footer_settings = FooterSettings.objects.first()
    footer_menus = {
        "main": FooterMenu.objects.filter(section="main"),
        "info": FooterMenu.objects.filter(section="info"),
        "resources": FooterMenu.objects.filter(section="resources"),
    }
    
    context = {
        "settings": settings,
        "form": signup_form,
        "subscriber_form": subscriber_form,
        "footer_settings": footer_settings,
        "footer_menus": footer_menus,
    }
    return render(request, "tradingapp/registrations/signup.html", context)


# Login View
def login_view(request):
    settings = SiteSettings.objects.first()
    login_form = LoginForm()
    subscriber_form = SubscriberForm()
    
    if request.method == "POST":
        login_form = LoginForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("home")
        else:
            messages.error(request, "Invalid login credentials.")
    
    # Footer
    footer_settings = FooterSettings.objects.first()
    footer_menus = {
        "main": FooterMenu.objects.filter(section="main"),
        "info": FooterMenu.objects.filter(section="info"),
        "resources": FooterMenu.objects.filter(section="resources"),
    }
    
    context = {
        "settings": settings,
        "form": login_form,
        "subscriber_form": subscriber_form,
        "footer_settings": footer_settings,
        "footer_menus": footer_menus,
    }
    return render(request, "tradingapp/registrations/login.html", context)

# Logout
def logout_view(request):
    logout(request)
    return redirect("login")