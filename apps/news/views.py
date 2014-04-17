import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View

from .models import *

__all__ = [
    'NewsList',
    'NewDetail',
    'PostLike'
]


class NewsList(ListView):
    model = New
    paginate_by = 5
    template_name = 'news/news_list.html'


class NewDetail(DetailView):
    model = New
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(NewDetail, self).get_context_data(**kwargs)
        can_like = False

        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')

        ip_list = self.get_object().like_set.all().values_list('ip', flat=True)
        if self.request.user.is_authenticated():
            can_like = True
        elif ip in ip_list:
            can_like = False
        else:
            can_like = True
        ctx.update(
            {
                'can_like': can_like,
            }
        )
        return ctx


class PostLike(View):
    def post(self, *args, **kwargs):
        fields = {}
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        fields['ip'] = ip
        if self.request.user:
            user = User.objects.get(username=self.request.user)
            fields['user'] = user
        if self.request.POST.get('object'):
            new_object = New.objects.get(id=self.request.POST.get('object'))
            fields['new'] = new_object
            Like.objects.create(**fields)
            return HttpResponse(json.dumps({'status': 200}), mimetype='application/json', status=400)
        return HttpResponse(json.dumps({'status': 400}), mimetype='application/json', status=400)



