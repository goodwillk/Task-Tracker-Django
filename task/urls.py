from django.urls import path
from task import views

# urlpatterns = [
#     path('list/', views.list, name='list_task'),
#     path('retrieve/<int:pk>', views.retrieve, name='retrieve_task'),
#     path('create/', views.create , name='create_task'),
#     path('update/<int:pk>', views.put , name='put_task'),
#     path('update_partial/<int:pk>', views.patch , name='patch_task'),
#     path('delete/<int:pk>', views.delete , name='delete_task'),
# ]

urlpatterns = [
    path('task/get/', views.TaskList.as_view()),
    path('task/post/', views.TaskList.as_view()),
    path('task/<int:pk>/get/', views.TaskSpecific.as_view()),
    path('task/<int:pk>/put/', views.TaskSpecific.as_view()),
    path('task/<int:pk>/patch/', views.TaskSpecific.as_view()),
    path('task/<int:pk>/delete/', views.TaskSpecific.as_view()),
    path('task/filter_estimate/get/', views.TaskEstimateFilterList.as_view()),
    path('task/filter_created/get/', views.TaskCreateFilterList.as_view()),
    
    path('task/filter_task/get/', views.TaskSearchFilterList.as_view()),
    # path('task/filter_est/get/', views.TaskFilterList.as_view({'get': 'list'})),          #Not Working View
]
        