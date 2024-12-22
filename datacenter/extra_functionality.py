from django.utils.timezone import localtime


SECONDS_HOUR = 3600
MINUTES_HOUR = 60
SECONDS_MINUTE = 60


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

    if total_time >= SECONDS_HOUR:
        total_hour = int(total_time / SECONDS_HOUR)
        total_time -= total_hour * SECONDS_HOUR

    total_min = total_time / MINUTES_HOUR
    return f'{total_hour}ч {int(total_min)}мин'


def suspicious_visit_time(time_minute=60):
    return time_minute * SECONDS_MINUTE
