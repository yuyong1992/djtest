# -*- coding: utf-8 -*-
# Created by YUYONG on 2021/6/5
from rest_framework import serializers
from djtest import models


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields = '__all__'


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Api
        fields = '__all__'


class NftSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NftToken
        fields = '__all__'


if __name__ == '__main__':
    pass
