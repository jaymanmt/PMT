from django.urls import path
from .views import howItWorks, blogPage, contactPage, faqPage, blogPost1, blogPost2, blogPost3

urlpatterns = [
    path("how", howItWorks, name="howItWorks"),
    path("about", blogPage, name="blogPage"),
    path("faq", faqPage, name="faqPage"),
    path("contact-us", contactPage, name="contactPage"),
    path("about/1", blogPost1, name="blogPost1"),
    path("about/2", blogPost2, name="blogPost2"),
    path("about/3", blogPost3, name="blogPost3")
]