from django.contrib import admin
from .models import PollModel
from .models import DemoModel
from .models import SocialMedia


admin.site.register(PollModel)
admin.site.register(DemoModel)
admin.site.register(SocialMedia)

