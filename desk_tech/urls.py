from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('confidential/', admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profile/", include("apps.profiles.urls")),
    path("api/v1/products/", include("apps.products.urls")),
    path("api/v1/ratings/", include("apps.ratings.urls")),

]

admin.site.site_header = "DeskTech Admin"
admin.site.site_title = "DeskTech Admin Portal"
admin.site.index_title = "Welcome to the DeskTech Portal"