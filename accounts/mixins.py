from django.shortcuts import get_object_or_404
from .models import *


# class FollowerAcceptMixin():
#     def dispatch(self, request, id, *args, **kwargs):
#         relation = get_object_or_404(Relation, id=id)
#         if relation.status == 'a':
#             return super().dispatch(*args, **kwargs)