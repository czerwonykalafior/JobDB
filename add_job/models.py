from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinLengthValidator
from django.forms import ModelForm

class Branza(models.Model):
    nazwa = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' %(self.nazwa.capitalize())
    class Meta:
        ordering = ['nazwa']

class Tag(models.Model):
    nazwa = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' %(self.nazwa.capitalize())

    class Meta:
        ordering = ['nazwa']

class Job(models.Model):
    stanowisko = models.CharField('stanowisko',max_length=100)
    branze = models.ManyToManyField(Branza, related_name="branze", related_query_name="branza")
    opis = models.TextField('opis', validators=[MinLengthValidator(200)], max_length=400, help_text='min. 200 znakow')
    tags = models.ManyToManyField(Tag, max_length=20)

    def __unicode__(self):
        return u'%s' % (self.stanowisko.capitalize())

    class Meta:
        ordering = ['stanowisko']
        verbose_name='stanowisko'
        verbose_name_plural= 'stanowiska'











# Create your models here.
