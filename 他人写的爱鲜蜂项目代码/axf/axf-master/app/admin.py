from django.contrib import admin

from app.models import Main, OrderGoodsModel, OrderModel, CartModel, Goods, FoodType, MainShow, MainWheel, MainNav, \
    MainShop, MainMustBuy

@admin.register(OrderGoodsModel)
class OrderGoodsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    pass


@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(MainShow)
class MainShowAdmin(admin.ModelAdmin):
    pass
@admin.register(MainWheel)
class MainWheelAdmin(admin.ModelAdmin):
    pass
@admin.register(MainNav)
class MainNavAdmin(admin.ModelAdmin):
    pass

@admin.register(MainMustBuy)
class MainMustBuyAdmin(admin.ModelAdmin):
    pass
@admin.register(MainShop)
class MainShopAdmin(admin.ModelAdmin):
    pass
