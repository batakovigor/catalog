"""catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.DemoWorksFilteredSingleTableView.as_view(), name='demowork_list'),
    url(r'^nofilter/$', views.DemoWorksSingleTableView.as_view() ),
    url(r'^filter2/$', views.FilteredTableView.as_view() ),
    url(r'^filter_ex/$', views.FilterExListView.as_view(), name='demowork_list_ex' ),
    path('new/', views.DemoWorksCreate, name='demowork_new'),
    path('view/<int:pk>', views.DemoWorksView, name='demowork_view'),
    path('edit/<int:pk>', views.DemoWorksUpdate, name='demowork_edit'),
    path('delete/<int:pk>', views.DemoWorksDelete, name='demowork_delete'),
    path('record/new/', views.RecordDemoWorksCreate, name='record_demowork_new'),
    path('record/view/<int:pk>', views.RecordDemoWorksView, name='record_demowork_view'),
    path('record/edit/<int:pk>', views.RecordDemoWorksUpdate, name='record_demowork_edit'),
    path('record/delete/<int:pk>', views.RecordDemoWorksDelete, name='record_demowork_delete'),
] + static(settings.MEDIA_URL, docoment_root=settings.MEDIA_ROOT)
