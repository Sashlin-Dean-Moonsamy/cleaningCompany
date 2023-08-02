from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm


# Create your views here.
@login_required
def dashboard(request):
    client_appointments = Appointment.objects.all().filter(user=request.user)
    return render(request, 'base/dashboard.html', {'appointments': client_appointments})


@login_required
def bookings(request):
    if request.POST:
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('base:bookings')  # Redirect to a success page after booking
        else:
            for errors in form.errors.values():
                for error in errors:
                    messages.error(request, f"{error}")
    form = AppointmentForm()
    return render(request, 'base/bookings.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect('home')
