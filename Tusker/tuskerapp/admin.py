from django.contrib import admin
from .models import Activity
from .models import ActivityTemplate
from .models import Relations
from .models import UserProfile

admin.site.register(Activity)
admin.site.register(ActivityTemplate)
admin.site.register(Relations)

admin.site.register(UserProfile)