from django.shortcuts import render
from website.models import SliderImage, AboutUs, ContactInfo, Project, WhatIsVastu, Review
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from website.forms import QueryForm
# Create your views here.


def home(request):
    """
        View for home page
    """
    context = {}
    context['slider_images'] = SliderImage.objects.order_by('-datetime')
    context['about_us'] = AboutUs.objects.first()
    context['contact_info'] = ContactInfo.objects.first()
    context['projects'] = Project.objects.order_by('-datetime')
    context['vastu'] = WhatIsVastu.objects.first()
    context['reviews'] = Review.objects.order_by('-datetime')
    context['form'] = QueryForm()
    return render(request, 'home.html', context)


@require_POST
def SubmitQueryView(request):
    """
        View function for submitting query form
    """
    if request.is_ajax():
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Query submitted successfully.'}, status=200)
        return JsonResponse(dict(form.errors), status=400)