from django.contrib import admin
from .models import affiliate
from .models import articles
from .models import promotions

admin.site.register(affiliate)
admin.site.register(articles)
admin.site.register(promotions)
