# tradingapp/admin.py
from django.contrib import admin
from .models import SiteSettings, Category, Post, FooterMenu, FooterSettings
from .models import HomeBanner
from .models import SectionBackground,Feature,HowItWorks,HowItWorksSection,DashboardBackground,CommunitySection,CommunityImage
from .models import AboutSection,AboutPage,AboutFeature
from .models import PartnerCity, PartnerRequest, PartnerPageContent,PartnerBenefit
from django.contrib.auth.admin import UserAdmin

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("id", "knowledge_title", "knowledge_highlight")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date")
    list_filter = ("category", "date")

@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ("logo_text",)

@admin.register(FooterMenu)
class FooterMenuAdmin(admin.ModelAdmin):
    list_display = ("title", "section")
    list_filter = ("section",)


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "highlight", "users_count")


@admin.register(SectionBackground)
class SectionBackgroundAdmin(admin.ModelAdmin):
    list_display = ("id", "background_image")  # only show id + image

from django.contrib import admin
from .models import HomeSection

@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "highlight_text")

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "highlight")
    list_editable = ("highlight",)

@admin.register(HowItWorksSection)
class HowItWorksSectionAdmin(admin.ModelAdmin):
    list_display = ("id", "background",)


@admin.register(HowItWorks)
class HowItWorksAdmin(admin.ModelAdmin):
    list_display = ("position", "title")
    ordering = ("position",)

@admin.register(DashboardBackground)
class DashboardBackgroundAdmin(admin.ModelAdmin):
    list_display = ("id", "background_image")  # only show id + image

@admin.register(CommunitySection)
class CommunitySectionAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(CommunityImage)
class CommunityImageAdmin(admin.ModelAdmin):
    list_display = ("id", "section", "order", "image")
    list_editable = ("order",)


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    readonly_fields = ('updated_at',)


@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

@admin.register(PartnerCity)
class PartnerCityAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(PartnerRequest)
class PartnerRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "city", "verified", "created_at")
    list_filter = ("verified", "city")
    search_fields = ("name", "phone", "email")

@admin.register(PartnerPageContent)
class PartnerPageContentAdmin(admin.ModelAdmin):
    list_display = ("heading",)

@admin.register(PartnerBenefit)
class PartnerBenefitAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "highlighted")
    list_editable = ("order", "highlighted")

