from django.db import models


# Create your models here.


class Module(models.Model):
    """
    模块表
    """
    name = models.CharField(verbose_name='模块名称', max_length=45, unique=True)
    sequence = models.IntegerField(verbose_name='显示顺序', default=0)

    class Meta:
        ordering = ['sequence']


class Api(models.Model):
    """
    接口表
    """
    name = models.CharField(verbose_name='接口名称', max_length=45)
    method = models.CharField(verbose_name='请求方法', max_length=45, default='GET')
    protocol = models.CharField(verbose_name='请求协议', max_length=10, default='HTTP')
    url = models.CharField(verbose_name='接口地址', max_length=256, default='')
    params = models.JSONField(verbose_name='查询参数', max_length=256, default=dict)
    header = models.JSONField(verbose_name='请求头信息', max_length=256, default=dict)
    body = models.JSONField(verbose_name='表单字段及描述信息', max_length=1024, null=True)
    types = (
        ('none', 'none'), ('multipart/form-data', 'mutipart/form-data'),
        ('x-www-form-urlencoded', 'x-www-form-urlencoded'),
        ('application/json', 'application/json'), ('binary', 'binary'))
    bodytype = models.CharField(verbose_name='消息体类型', max_length=30, choices=types, default='none')
    status = models.CharField(verbose_name='接口状态', max_length=4, choices=(('1', '启用'), ('2', '禁用'), ('3', '废弃')),
                              default='启用')
    ceratetime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updatetime = models.DateTimeField(verbose_name='更新时间')
    isbase = models.CharField(verbose_name='是否基线化', max_length=4, choices=(('1', '是'), ('2', '否')), default='否')
    module = models.ForeignKey(verbose_name='所属模块', on_delete=models.CASCADE, to=Module)

    class Meta:
        ordering = ['updatetime']