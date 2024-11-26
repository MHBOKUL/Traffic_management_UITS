from django.contrib import admin
from .models import LicenceOwner, Fine, Expiry

admin.site.register(LicenceOwner)
admin.site.register(Fine)
admin.site.register(Expiry)
