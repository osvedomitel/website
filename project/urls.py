from django.contrib import admin
from django.urls import path

import news.views


urlpatterns = [
    path('', news.views.home, name='home'),
    path('<int:year>/<int:month>/', news.views.issue, name='issue'),
    path('<int:year>/<int:month>/<str:slug>/', news.views.article, name='article'),
    path('броеве/', news.views.all_issues, name='all-issues'),
    path('рубрики/<str:slug>/', news.views.category, name='category'),
    path('ключови-думи/<str:slug>/', news.views.keyword, name='keyword'),

    path('admin/', admin.site.urls),
]
