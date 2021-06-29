from django.contrib import admin
from django.http import HttpResponseRedirect

from postsapp.models import Publication


@admin.register(Publication)
class VillainAdmin(admin.ModelAdmin):

    change_form_template = "custom_admin/pubs-change-forms.html"

    def response_change(self, request, obj):
        if "_del-comments" in request.POST:
            obj.comment.all().delete()
            self.message_user(request, "Все коментарии удалены")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)
