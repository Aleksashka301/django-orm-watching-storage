from django.utils.timezone import localtime


def get_duration(visit):
    visit_in = localtime(visit.entered_at)
    if not visit.leaved_at:
        visit_out = localtime()
    else:
        visit_out = localtime(visit.leaved_at)

    return visit_out - visit_in


def format_duration(visit):
    SEC_HOUR = 3600
    MIN_HOUR = 60

    total_time = visit.total_seconds()
    total_hour = 0

    if total_time >= SEC_HOUR:
        total_hour = int(total_time / SEC_HOUR)
        total_time -= total_hour * SEC_HOUR

    total_min = total_time / MIN_HOUR
    return f'{total_hour}ч {int(total_min)}мин'


def calculation_time(time_minute=60):
    SEC_MINUTE = 60
    return time_minute * SEC_MINUTE
