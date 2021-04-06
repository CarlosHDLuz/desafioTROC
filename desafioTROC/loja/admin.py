from django.contrib import admin

from .models import Produto, CupomFixo, CupomPercentual

admin.site.register(Produto)
admin.site.register(CupomFixo)
admin.site.register(CupomPercentual)

