from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment')
    readonly_fields = ('comment_dt', )
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('order_name',)
    search_fields = ('order_name', 'order_phone')
    list_filter = ('order_status', )
    list_editable = ('order_status', 'order_phone')
    list_per_page = 10
    list_max_show_all = 100
    readonly_fields = ('id', 'order_dt')
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')

    inlines = [Comment,]

admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)

