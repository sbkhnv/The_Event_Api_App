from django.shortcuts import render
from django.views import View
from event.models import Schedule,Speakers,Sponsors,Hotels,Tickets,Gallery


# class LandingPageView(View):
#     def get(self,request):
#         return render(request,"index.html")
#
#     def post(self, request):
#         form = UserLoginForm()
#         context = {'form': form}
#         return render(request, 'users/login.html', context)


class IndexView(View):
    def get(self, request):
        schedule = Schedule.objects.all()
        sponsors = Sponsors.objects.all()
        speakers = Speakers.objects.all()
        tickets = Tickets.objects.all()
        gallery = Gallery.objects.all()
        hotels = Hotels.objects.all()
        search = request.GET.get('search')
        if not search:

            context = {
                'schedule': schedule,
                'sponsors': sponsors,
                'speakers': speakers,
                'tickets': tickets,
                'gallery': gallery,
                'hotels':hotels,
            }
        else:
            products = Speakers.objects.filter(first_name__icontains=search)
            if not products:
                return TypeError
            else:
                context = {
                    'schedule': schedule,
                'sponsors': sponsors,
                'speakers': speakers,
                'tickets': tickets,
                'gallery': gallery,
                'hotels':hotels,
                }

                return render(request, 'index.html',  context)

        products = Speakers.objects.all()
        context = {
            'schedule': schedule,
                'sponsors': sponsors,
                'speakers': speakers,
                'tickets': tickets,
                'gallery': gallery,
                'hotels':hotels,
        }
        return render(request, 'index.html', context)

    # def post(self, request):
    #     form = UserLoginForm()
    #     context = {'form': form}
    #     return render(request, 'users/login.html', context)



