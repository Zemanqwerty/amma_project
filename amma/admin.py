from django.contrib import admin
from .models import Application, ActiveCertificate, Workers, Massages, Spa, Spafortwo, ActiveAboniment, Aboniment, Photo
from .models import Hamam, Hidromassage, Salt

# Register your models here.

admin.site.register(Application)
admin.site.register(ActiveCertificate)
admin.site.register(Workers)
admin.site.register(Massages)
admin.site.register(Spa)
admin.site.register(Spafortwo)
admin.site.register(ActiveAboniment)
admin.site.register(Aboniment)
admin.site.register(Photo)
admin.site.register(Hamam)
admin.site.register(Hidromassage)
admin.site.register(Salt)
