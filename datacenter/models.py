from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


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

