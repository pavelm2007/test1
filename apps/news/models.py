# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

__all__ = [
    'New',
    'Like'
]


class New(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    created = models.DateField(u'Дата создания', auto_now_add=True)
    content = models.CharField(u'Текст', max_length=140, help_text=u'Не более 140 символов')

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'detail', (), {'pk': self.id, }


class Like(models.Model):
    ip = models.IPAddressField(u'IP адрес')
    created = models.DateField(u'Дата создания', auto_now_add=True)
    new = models.ForeignKey(New)
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'

