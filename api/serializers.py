from rest_framework.serializers import ModelSerializer
from .models import *

class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDolist
        fields = '__all__'
