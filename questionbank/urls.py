from django.contrib import admin
from django.urls import path, include
from papers.views import signup, CustomLoginView, welcome  # ✅ Fix this: use 'welcome' instead of 'welcome_page'
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', welcome, name='welcome'),  # ✅ Use your correct view function name
    path('admin/', admin.site.urls),
    path('papers/', include('papers.urls')),

    # Authentication
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
