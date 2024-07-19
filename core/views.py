from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Record
from .forms import NewRecordFrom, UpdateRecordFrom


def home(request):
    context = {}
    return render(request, "core/home.html", context)


@login_required
def dashboard(request):
    records = Record.objects.filter(created_by=request.user)
    # if request.user != record.created_by:
        # return redirect("core:home")

    context = {"records": records}
    return render(request, "core/dashboard.html", context)


@login_required
def create_record(request):
    form = NewRecordFrom()

    if request.method == "POST":
        form = NewRecordFrom(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.created_by = request.user
            record.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Record for {username} created successfully!')
            return redirect("core:dashboard")

    context = {
        "form": form,
        "title": "Create a new record"
    }
    return render(request, "core/record_form.html", context)


def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)

    context = {
        "record": record,
    }
    return render(request, "core/record_detail.html", context)


@login_required
def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk)

    form = UpdateRecordFrom(instance=record)

    if request.method == "POST":
        form = UpdateRecordFrom(request.POST, instance=record)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            messages.success(request, f'Record for {username} was updated successfully!')
            return redirect("core:dashboard")

    context = {
        "form": form,
        "record": record,
        "title": "Update record",
    }
    return render(request, "core/record_form.html", context)


@login_required
def delete(request, pk):
    record = get_object_or_404(Record, pk=pk)

    if request.method == "POST":
        record.delete()

        messages.success(request, f'Record deleted successfully!')
        return redirect("core:dashboard")

    context = {"record": record}
    return render(request, "core/delete_record.html", context)
