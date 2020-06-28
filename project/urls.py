from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, register_converter

import news.views
from project import converters


register_converter(converters.YearConverter, 'yyyy')
register_converter(converters.MonthConverter, 'mm')


urlpatterns = [
    path('', news.views.home, name='home'),
    path('<yyyy:year>/<mm:month>/', news.views.issue, name='issue'),
    path('<yyyy:year>/<mm:month>/<str:slug>/', news.views.article, name='article'),
    path('броеве/', news.views.all_issues, name='all-issues'),
    path('рубрики/<str:slug>/', news.views.category, name='category'),
    path('ключови-думи/<str:slug>/', news.views.keyword, name='keyword'),
    path('avtori/<str:slug>/', news.views.author, name='author'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
