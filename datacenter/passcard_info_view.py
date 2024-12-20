from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.extra_functionality import get_duration
from datacenter.extra_functionality import format_duration
from datacenter.extra_functionality import calculation_time
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in visits:
        total_time = get_duration(visit)
        visit_info = {
            'entered_at': visit.entered_at,
            'duration': format_duration(total_time),
            'is_strange': total_time.total_seconds() >= calculation_time(60),
        }
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
    }

    return render(request, 'passcard_info.html', context)



