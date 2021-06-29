import json

from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from postsapp.forms import PubCreateForm
from postsapp.models import Publication, Comments
from django.contrib import messages


class StartPageView(View):
    template_name = 'postsapp/start-page.html'

    def get(self, request, *args, **kwargs):
        context = {}
        pubs = Publication.objects.order_by('-date')
        context.update({'pubs': pubs})
        return render(request, self.template_name, context)


class CreatePubView(View):
    template_name = 'postsapp/create-pub-page.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        context = {}
        form = PubCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.user = request.user
            instance.save()
            messages.success(request, 'Успешно опубликовано')
            return redirect('start-page')
        else:
            messages.error(request, 'Ошибка при создании публикации, проверте, все ли поля заполнены.')
        return render(request, self.template_name, context)


class UserPubsView(View):
    template_name = 'postsapp/users-pub-page.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pubs = request.user.publication.order_by('-date')
        context = {'pubs': pubs}
        return render(request, self.template_name, context)


class ChangePubView(View):
    template_name = 'postsapp/pub-edit-page.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pub = Publication.objects.get(id=self.kwargs['pid'])
        if request.user == pub.user:
            context = {'pub': pub}
            return render(request, self.template_name, context)
        else:
            messages.error(request, 'Отказано в доступе')
            return redirect('start-page')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        context = {}
        pub = Publication.objects.get(id=self.kwargs['pid'])
        form = PubCreateForm(request.POST, request.FILES, instance=pub)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешно отредактировано :)')
            return redirect('user-pubs-page')
        else:
            context.update({'form': form})
        return render(request, self.template_name, context)


@login_required
def add_pub(request):
    if request.POST:
        form = PubCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.user = request.user
            instance.save()

            data_response = {
                'success': True,
                'img': instance.img.url,
                'title': instance.title,
                'text': instance.text,
                'date': instance.date.strftime('%Y-%m-%d %H:%M'),
                'pub_id': instance.id,
                'first_name': instance.user.first_name,
                'last_name': instance.user.last_name
            }
        else:
            data_response = {'success': False}
        return HttpResponse(json.dumps(data_response, cls=DjangoJSONEncoder), content_type='application/json')


@login_required
def add_comment(request):
    if request.POST:
        pub = Publication.objects.get(id=request.POST.get('pubid'))
        comm = Comments.objects.create(author=request.user,
                                       text=request.POST.get('comment'),
                                       publication=pub)
        comm.save()
        data_response = {'success': True}
        return HttpResponse(json.dumps(data_response), content_type='application/json')


@login_required
def del_pub(request):
    if request.POST:
        pub = Publication.objects.get(id=request.POST.get('pubid'))
        pub.delete()
        data_response = {'success': True}
        return HttpResponse(json.dumps(data_response), content_type='application/json')


