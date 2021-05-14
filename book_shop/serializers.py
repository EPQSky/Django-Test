from rest_framework import serializers

from book_shop.models import Role


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('url', 'role_name', 'role_code')
