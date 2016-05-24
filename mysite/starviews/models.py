# coding: utf-8
from django.db import models

class stars(models.Model):
    """評価"""
    id = models.IntegerField(primary_key=True)
    star_level = models.IntegerField("対応評価")
    fix_time = models.IntegerField("対応時間")
