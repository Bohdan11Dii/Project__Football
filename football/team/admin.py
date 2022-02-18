from django.contrib import admin

from .models import Model
from .models import Contact

admin.site.register(Model)

admin.site.register(Contact)
