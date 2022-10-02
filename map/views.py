# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import Search
# from .forms import SearchForm
# import folium
# import geocoder

# # Create your views here.


# def index(request):
#         return HttpResponse('You address input is invalid')

#     # Create Map Object
#     m = folium.Map(location=[19, -12], zoom_start=2)

#     folium.Marker([lat, lng], tooltip='Click for more',
#                   popup=country).add_to(m)
#     # Get HTML Representation of Map Object
#     m = m._repr_html_()
#     context = {
#         'm': m,
#         'form': form,
#     }
#     return render(request, 'index.html', context)

# from django.shortcuts import render, redirect
from django.http import HttpResponse
# import folium
# import geocoder

# Create your views here.


def index(request):
    return HttpResponse('You address input is invalid')