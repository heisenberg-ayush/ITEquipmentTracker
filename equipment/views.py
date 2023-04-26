from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipment
from .forms import EquipmentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/inventory.html', {'equipments': equipments})

@login_required
def add_equipment(request):
    form = EquipmentForm()
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid:
            equipment = form.save(commit=False)
            equipment.save()
            return redirect('index')
    else:
        form = EquipmentForm()

    return render(request, 'equipment/add_equipment.html', {'form': form})

@login_required
def edit_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid:
            equipment = form.save(commit=False)
            equipment.save()
            return redirect('equipment/inventory.html', pk=equipment.pk)
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'edit_equipment.html', {'form': form})

@login_required
def delete_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.delete()
    return redirect('index')