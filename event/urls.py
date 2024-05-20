from django.urls import path,include
from .views import SpeakersApiView,ScheduleApiView,SponsorsApiView,HotelsApiView,TicketsApiView,GalleryApiView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register("schedule",viewset=ScheduleApiView)
router.register("speakers",viewset=SpeakersApiView)
router.register("sponsors",viewset=SponsorsApiView)
router.register("hotels",viewset=HotelsApiView)
router.register("tickets",viewset=TicketsApiView)
router.register("gallery",viewset=GalleryApiView)

urlpatterns = [
    path("",include(router.urls)),
    path("auth/",views.obtain_auth_token),
]