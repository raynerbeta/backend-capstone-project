from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("tables", views.BookingViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.MenuItemView.as_view()),
    path(
        "restaurant/booking/",
        include(router.urls),
    ),
]
