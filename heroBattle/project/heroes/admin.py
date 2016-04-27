from django.contrib import admin
from heroes.models import Leader, Power

# Register your models here.

class LeaderModelAdmin(admin.ModelAdmin):
	list_display = ["first_name", "last_name"]
	search_fields = ["first_name", "last_name"]

	class Meta:
		model = Leader


class PowerModelAdmin(admin.ModelAdmin):
	list_display = ["name", "method"]
	search_fields = ["name", "method"]

	class Meta:
		model = Power

admin.site.register(Leader, LeaderModelAdmin)
admin.site.register(Power, PowerModelAdmin)

