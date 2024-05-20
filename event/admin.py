from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from event.models import Gallery,Speakers,Sponsors,Schedule,Hotels,Tickets

admin.site.register([Gallery,Speakers,Sponsors,Schedule,Tickets,Hotels])
