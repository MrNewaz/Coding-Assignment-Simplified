from django.urls import path
from .views import *

urlpatterns = [
    path('child/', ChildListApiView.as_view(),
         name="child-user-list"),  # child data list
    path('child/create/', ChildCreateApiView.as_view(),
         name="child-user-create"),  # create child user
    path('child/delete/<id>/', ChildDestroyApiView.as_view(),
         name="child-user-delete"),  # delete child
    path('child/update/<id>/', ChildUpdateApiView.as_view(),
         name="child-user-update"),  # update child

    path('parent/', ParentListApiView.as_view(),
         name="parent-user-list"),  # parent data list
    path('parent/create/', ParentCreateApiView.as_view(),
         name="parent-user-create"),

    # create parent user
    path('parent/delete/<id>/', ParentDestroyApiView.as_view(),
         name="parent-user-delete"),  # delete parent
    path('parent/update/<id>/', ParentUpdateApiView.as_view(),
         name="parent-user-update"),  # update parent
]
