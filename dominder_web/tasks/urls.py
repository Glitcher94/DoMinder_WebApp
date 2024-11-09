from django.urls import path
from .views import TareaList, TareaCreate, TareaUpdate, TareaDelete

urlpatterns = [
    path('tasks/', TareaList.as_view(), name='task-list'),  # GET
    path('tasks/create/', TareaCreate.as_view(), name='task-create'),  # POST
    path('tasks/update/<int:pk>/', TareaUpdate.as_view(), name='task-update'),  # PUT
    path('tasks/delete/<int:pk>/', TareaDelete.as_view(), name='task-delete'),  # DELETE
]
