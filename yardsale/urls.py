from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = [
    url(r'^$', views.follower_list, name='home'),
    url(r'^follower/(?P<pk>\d+)$', views.follower_warnings, name='warning'),
    url(r'^warnings/(?P<pk>[0-9]+)/new', views.new_warn, name='new_warn'),
    url(r'^warnings/(?P<pk>[0-9]+)/edit$', views.edit_warn, name='edit_warn'),
    url(r'^follower/(?P<pk>[0-9]+)/edit', views.follower_edit, name='follower_edit'),
    url(r'^register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
#     url(r'^accounts/password_change/done/', 'django.contrib.auth.views.password_change_done', {'template_name':'registration/completed.html'}),
    url(r'^accounts/', include('django.contrib.auth.urls'),
#         {'template_name':'registration/register.html'}
        ),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)