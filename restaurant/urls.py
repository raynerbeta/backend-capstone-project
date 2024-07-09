from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("tables", views.BookingViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("menu-items", views.MenuItemsView.as_view()),
    path("menu-items/<int:pk>", views.MenuItemView.as_view()),
    path(
        "restaurant/booking/",
        include(router.urls),
    ),
]
