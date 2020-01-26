from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Hotel, Summary


def index(request):
    all_hotels = Hotel.objects.all()
    context = {
        'all_hotels': all_hotels,
    }
    return render(request, 'abcr_home/index.html', context)


def show(request):

    if request.method == 'GET' and 'hotel_id' in request.GET:
        hotel_id = request.GET['hotel_id']
        if hotel_id is not None and hotel_id != '':
            all_hotels = Hotel.objects.all()
            selected_hotel = Hotel.objects.get(pk=request.GET['hotel_id'])
            summaries_selected_hotel = selected_hotel.summary_set.all()
            aspects_for_this_hotel = summaries_selected_hotel.values('aspect').distinct()
            selected_aspects_for_this_hotel = aspects_for_this_hotel
            context = {
                'all_hotels': all_hotels,
                'selected_hotel': selected_hotel,
                'summaries_selected_hotel': summaries_selected_hotel,
                'aspects_for_this_hotel': aspects_for_this_hotel,
                'selected_aspects_for_this_hotel': selected_aspects_for_this_hotel,
            }
            return render(request, 'abcr_home/index.html', context)

    else:
        all_hotels = Hotel.objects.all()
        button_pressed_wrongly =1
        context = {
            'all_hotels': all_hotels,
            'button_pressed_wrongly' : button_pressed_wrongly,
        }
        return render(request, 'abcr_home/index.html', context)

        '''all_hotels = Hotel.objects.all()
        selected_hotel = Hotel.objects.get(pk=request.GET['hotel_id'])
        summaries_selected_hotel = selected_hotel.summary_set.all()
        aspects_for_this_hotel = summaries_selected_hotel.values('aspect').distinct()
        selected_aspects_for_this_hotel = aspects_for_this_hotel
        context = {
            'all_hotels': all_hotels,
            'selected_hotel': selected_hotel,
            'summaries_selected_hotel': summaries_selected_hotel,
            'aspects_for_this_hotel' : aspects_for_this_hotel,
            'selected_aspects_for_this_hotel' : selected_aspects_for_this_hotel,
        }
        return render(request, 'abcr_home/index.html', context)'''

def show_2(request):
    all_hotels = Hotel.objects.all()
    selected_hotel = Hotel.objects.get(pk=request.GET['hotel_id'])
    summaries_selected_hotel = selected_hotel.summary_set.all()
    aspects_for_this_hotel = summaries_selected_hotel.values('aspect').distinct()
    selected_aspects_for_this_hotel = request.GET.getlist('list_of_selected_aspects[]')

    aspects_temp_list = []
    for aspect in selected_aspects_for_this_hotel:
        temp_dict = {}
        temp_dict['aspect']=aspect
        aspects_temp_list.append(temp_dict)

    context = {
        'all_hotels': all_hotels,
        'selected_hotel': selected_hotel,
        'summaries_selected_hotel': summaries_selected_hotel,
        'aspects_for_this_hotel' : aspects_for_this_hotel,
        'selected_aspects_for_this_hotel': aspects_temp_list,

    }
    return render(request, 'abcr_home/index.html', context)