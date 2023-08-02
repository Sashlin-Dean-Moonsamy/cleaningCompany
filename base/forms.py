from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['team', 'date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        team = cleaned_data.get('team')
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        # Check if there are any existing appointments for the selected team and date
        existing_appointments = Appointment.objects.filter(
            team=team,
            date=date,
        )

        for appointment in existing_appointments:
            if (appointment.start_time <= start_time <= appointment.end_time) or \
                    (appointment.start_time <= end_time <= appointment.end_time):
                raise ValidationError(
                    _('The team is already booked for this date and time. Please choose another date/time.')
                )

        return cleaned_data
