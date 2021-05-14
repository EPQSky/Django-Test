# Create your views here.
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets

from book_shop import models
from book_shop.models import Role
from book_shop.serializers import RoleSerializer


def index(request):
    latest_role_list = models.Role.objects.order_by('-id')[:5]
    context = {
        'latest_role_list': latest_role_list,
    }
    return render(request, 'book_shop/index.html', context)


def detail(request, role_id):
    try:
        role = models.Role.objects.get(id=role_id)
    except models.Role.DoesNotExist:
        raise Http404("Role does not exist")
    return render(request, 'book_shop/detail.html', {'role': role})


class RoleViewSet(viewsets.ModelViewSet):
    """
    用户查看角色信息
    """
    queryset = Role.objects.all().order_by('-id')
    serializer_class = RoleSerializer
