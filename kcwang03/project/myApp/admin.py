from django.contrib import admin

# Register your models here.

from  .models import Grades, Students


# 注册
class StudentsInfo(admin.TabularInline): # StackedInline
    model = Students
    extra = 2
class GradesAamin(admin.ModelAdmin):
    inlines = [StudentsInfo]

    # 列表页属性
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 2

    # 添加修改页属性
    # fields = ['ggirlnum', 'gboynum','gname','gdate', 'isDelete']
    fieldsets =[
        ("num", {"fields":['ggirlnum', 'gboynum']}),
        ('base', {"fields":['gname', 'gdate', 'isDelete']})
    ]

admin.site.register(Grades,GradesAamin)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"

    # 设置页面列的名称
    gender.short_description = "性别"



    list_display = ['pk', 'sname', 'sage', gender  ,'scontend', 'sgrade', 'isDelete']
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
# admin.site.register(Students, StudentsAdmin)