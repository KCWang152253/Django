from django.contrib import admin

from user.models import UserModel, UserTicketModel


@admin.register(UserModel)
class UserModelModelAdmin(admin.ModelAdmin):
    pass


@admin.register(UserTicketModel)
class UserTicketModelAdmin(admin.ModelAdmin):
    pass
