from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipment
from .forms import EquipmentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    equipments = Equipment.objects.all()
    query = request.GET.get('q')
    if query:
        equipments = Equipment.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        equipments = Equipment.objects.all()
        
    return render(request, 'equipment/inventory.html', {'equipments': equipments})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def edit_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid:
            equipment = form.save(commit=False)
            equipment.save()
            return redirect('index')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'equipment/edit_equipment.html', {'form': form})

@login_required(login_url='/login/')
def delete_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.delete()
    return redirect('index')

@login_required(login_url='/login/')
def equipment_list(request):
    query = request.GET.get('q')
    if query:
        equipments = Equipment.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        equipments = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipments': equipments})
