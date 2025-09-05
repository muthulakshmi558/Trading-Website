from django.urls import path
from . import views
# from .views import register_view, login_view

urlpatterns = [
    # path('', views.home, name='home'),   # homepage
        path("", views.home, name="home"),

    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),

    path("become-a-partner/", views.become_partner, name="become_partner"),
    path("verify-otp/<int:partner_id>/", views.verify_otp, name="verify_otp"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]