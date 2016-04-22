from django.contrib import admin
from heroes.models import Leader

# Register your models here.

class LeaderModelAdmin(admin.ModelAdmin):
	list_display = ["first_name", "last_name"]
	search_fields = ["first_name", "last_name"]

	class Meta:
		model = Leader

admin.site.register(Leader, LeaderModelAdmin)

