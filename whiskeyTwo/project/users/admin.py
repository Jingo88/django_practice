from django.contrib import admin
from users.models import User

# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
	list_display = ["username", "first_name", "last_name"]

	class Meta:
		model = User

admin.site.register(User, UserModelAdmin)