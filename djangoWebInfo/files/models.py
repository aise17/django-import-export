# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
 
class Document(models.Model):
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='imputCsv/%Y/%m/%d')


