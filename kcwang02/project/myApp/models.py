from django.db import models

# Create your models here.


class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default = False)
    def __str__(self):
        return self.gname
    class Meta:
        db_table = "grades"
        ordering = ['id']

class StudentsManager(models.Manager):
    def get_queryset(self):
        return  super(StudentsManager, self).get_queryset().filter(isDelete=False)

class Students(models.Model):
    # 自定义模型管理器
    stuObj = models.Manager()
    stuObj2 = StudentsManager()
    sname =models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField(db_column="age")
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)
    def __str__(self):
        return self.sname

    lastTime = models.DateTimeField(auto_now= True)
    createTime = models.DateTimeField(auto_now_add= True)
    class Meta:
        db_table = "students"
        ordering = ['id']