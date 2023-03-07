from django.contrib import admin

from .models import Posts


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        'text',
        'image'
    )
    list_editable = ("text", )

admin.site.register(Posts, PostAdmin)

