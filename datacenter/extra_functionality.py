from django.utils.timezone import localtime


def get_duration(visit):
    visit_in = localtime(visit.entered_at)
    if not visit.leaved_at:
        visit_out = localtime()
    else:
        visit_out = localtime(visit.leaved_at)

    return visit_out - visit_in


def format_duration(visit):
    total_time = visit.total_seconds()
    total_hour = 0

    if total_time >= 3600:
        total_hour = int(total_time / 3600)
        total_time -= total_hour * 3600

    total_min = total_time / 60
    return f'{total_hour}ч {int(total_min)}мин'
