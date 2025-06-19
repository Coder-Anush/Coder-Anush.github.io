from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_paper, name='upload'),
    path('upload-success/', views.upload_success, name='upload_success'),
    path('view/', views.view_papers, name='view_papers'),
    path('my-uploads/', views.my_uploads, name='my_uploads'),
    path('become-uploader/', views.become_uploader, name='become_uploader'),  # ✅ Required
    path('admin-info/', views.admin_info, name='admin_info'),  # ✅ Required
    path('download/<int:paper_id>/', views.download_paper, name='download_paper'),
]
