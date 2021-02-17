from django.urls import path, reverse_lazy
from .views import *
from allauth.account.views import login, logout
from django.conf.urls.static import static
from django.conf import settings

app_name = 'p_library'

urlpatterns = [
    path('lib/', lib),
    path('test/', test),
    path('', index, name='index'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('books/', BookList.as_view(), name='book_list'),
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(template_name='p_library/register.html', success_url=reverse_lazy('p_library:profile-create')), name='register'),  
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)