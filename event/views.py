from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.transaction import atomic
from django.shortcuts import render
from django.views import View
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Speakers,Schedule,Sponsors,Hotels,Tickets,Gallery
from .serializers import SpeakersSerializer,ScheduleSerializer,SponsorsSerializer,GallerySerializer,HotelsSerializer,TicketsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters, status
from rest_framework.filters import SearchFilter


# class SpeakersModalViewSet(ModelViewSet):
#     queryset = Speakers.objects.all()
#     serializer_class = SpeakersSerializer
#     permission_classes = (IsAuthenticated, )
#     filter_backends = (filters.SearchFilter, )
#     search_fields = ['first_name', ]
#     pagination_class = LimitOffsetPagination

# class IndexView(LoginRequiredMixin, View):
#     def get(self, request):
#         speakers = Speakers.objects.all()
#         schedule = Schedule.objects.all()
#         sponsors = Sponsors.objects.all()
#         gallery = Gallery.objects.all()
#         tickets = Tickets.objects.all()
#         hotels = Hotels.objects.all()
#
#         context = {
#             'speakers': speakers,
#             'schedule': schedule,
#             'sponsors': sponsors,
#             'gallery': gallery,
#             'tickets': tickets,
#             'hotels': hotels,
#         }
#         return render(request, 'index.html', context)



class SpeakersApiView(ModelViewSet):
    queryset = Speakers.objects.all()
    serializer_class = SpeakersSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, ]
    filter_backends = (filters.SearchFilter, )
    search_fields = ["first_name","last_name"]
    pagination_class = LimitOffsetPagination
    # def get(self,request):
    #     speakers = Speakers.objects.all()
    #     serializer = SpeakersSerializer(speakers,many=True)
    #     return Response(data=serializer.data)
    #
    #
    # def post(self,request,format=None):
    #     serializer = SpeakersSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def put(self, request, pk,format=None):
    #     obj = Speakers.objects.get(pk=pk)
    #     serializer = SpeakersSerializer(obj,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def patch(self, request,format=None):
    #     obj = Speakers.objects.get()
    #     serializer = SpeakersSerializer(obj,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )



class ScheduleApiView(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ["first_name","last_name"]
    pagination_class = LimitOffsetPagination
    # def get(self,request):
    #     schedule = Schedule.objects.all()
    #     serializer = ScheduleSerializer(schedule,many=True)
    #     return Response(data=serializer.data)
    #
    # def post(self,request,format=None):
    #     serializer = ScheduleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def put(self, request, pk,format=None):
    #     obj = Schedule.objects.get(pk=pk)
    #     serializer = ScheduleSerializer(obj,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def patch(self, request, pk,format=None):
    #     obj = Schedule.objects.get(pk=pk)
    #     serializer = ScheduleSerializer(obj,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )


class SponsorsApiView(ModelViewSet):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    permission_classes = LimitOffsetPagination
    # def get(self,request):
    #     sponsors = Sponsors.objects.all()
    #     serializer = SponsorsSerializer(sponsors,many=True)
    #     return Response(data=serializer.data)
    #
    # def post(self,request,format=None):
    #     serializer = SponsorsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def put(self, request, pk,format=None):
    #     obj = Sponsors.objects.get(pk=pk)
    #     serializer = SponsorsSerializer(obj,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def patch(self, request, pk,format=None):
    #     obj = Sponsors.objects.get(pk=pk)
    #     serializer = SponsorsSerializer(obj,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )


class HotelsApiView(ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ["name"]
    pagination_class = LimitOffsetPagination
    # def get(self,request):
    #     hotels = Hotels.objects.all()
    #     serializer = HotelsSerializer(hotels,many=True)
    #     return Response(data=serializer.data)
    #
    #
    # def post(self,request,format=None):
    #     serializer = HotelsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def put(self, request, pk,format=None):
    #     obj = Hotels.objects.get(pk=pk)
    #     serializer = HotelsSerializer(obj,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def patch(self, request, pk,format=None):
    #     obj = Hotels.objects.get(pk=pk)
    #     serializer = HotelsSerializer(obj,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )


class TicketsApiView(ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ["type"]
    pagination_class = LimitOffsetPagination


    @action(detail=True,methods=["POST"])
    def counted(self,request,*args,**kwargs):
        ticket = self.get_object()
        with atomic():
            ticket.count += 1
            ticket.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=False,methods=["GET"])
    def popular(self,request,*args,**kwargs):
        ticket = self.get_queryset()
        ticket = ticket.order_by('-count')[:3]
        serializer = TicketsSerializer(ticket,many=True)
        return Response(data=serializer.data)



    # def get(self,request):
    #     tickets = Tickets.objects.all()
    #     serializer = TicketsSerializer(tickets,many=True)
    #     return Response(data=serializer.data)
    #
    #
    # def post(self,request,format=None):
    #     serializer = TicketsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def put(self, request, pk,format=None):
    #     obj = Tickets.objects.get(pk=pk)
    #     serializer = TicketsSerializer(obj,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def patch(self, request, pk,format=None):
    #     obj = Tickets.objects.get(pk=pk)
    #     serializer = TicketsSerializer(obj,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )



class GalleryApiView(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    pagination_class = LimitOffsetPagination

    # def get(self,request):
    #     gallery = Gallery.objects.all()
    #     serializer = GallerySerializer(gallery,many=True)
    #     return Response(data=serializer.data)
    #
    #
    # def post(self,request,format=None):
    #     serializer = TicketsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def put(self, request, pk,format=None):
    #     obj = Tickets.objects.get(pk=pk)
    #     serializer = TicketsSerializer(obj,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def patch(self, request, pk,format=None):
    #     obj = Tickets.objects.get(pk=pk)
    #     serializer = TicketsSerializer(obj,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )


