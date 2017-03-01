from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.admin import TimtecUserAdmin
from politica_publica_social.models import SindsepProfile

User = get_user_model()

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class SindsepProfileInline(admin.StackedInline):
    model = SindsepProfile
    can_delete = False
    verbose_name_plural = 'Sindesep'

# Define a new User admin
class SindesepUserAdmin(TimtecUserAdmin):
    inlines = (SindsepProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, SindesepUserAdmin)
