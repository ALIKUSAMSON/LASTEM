from django.contrib import admin
from .models import AcademicModel, ClubsModel, EventsModel, SportsModel
# Register your models here.

# Register your models here.
admin.site.register(SportsModel)
admin.site.register(ClubsModel)
admin.site.register(EventsModel)
admin.site.register(AcademicModel)