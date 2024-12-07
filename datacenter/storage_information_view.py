from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, format_duration
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []
    active_visits = Visit.objects.all().filter(leaved_at__isnull=True)

    for visit in active_visits:
        visit_info = {
            'who_entered': visit.passcard,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit))
        }
        non_closed_visits.append(visit_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
