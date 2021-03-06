from django.shortcuts import get_object_or_404, render

from pages.models import Page


def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page.html', {'page': page})
