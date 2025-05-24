from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import ApplyScan, CounsellingBook, RegFreevig, Comments, PatHealthRec
from .forms import ApplyScanForm, CounsellingBookForm, RegFreevigForm, CommentsForm, PatHealthRecForm
from administrator.forms import District
from administrator.models import ScanCenter

from administrator.models import ScanType
from django.http import HttpResponse
from .models import ApplyScan, Patient
from administrator.models import GuideLines


def homee(request):
    # return HttpResponse("hai<br>"
    #                     "<a href='pat_health_rec_list_create'>Click me</a><br>"
    #                     "<a href='apply_scan_list_create'>Click me</a><br>"
    #                     "<a href='counselling_book_list_create'>Click me</a><br>"
    #                     "<a href='reg_freevig_list_create'>Click me</a><br>"
    #                     "<a href='comments_list_create'>Click me</a><br>"
    #                     )
    return render(request, 'patient_home.html')
# PatHealthRec
def pat_health_rec_list_create(request):
    if request.method == 'POST':
        form = PatHealthRecForm(request.POST,request.FILES)
        if form.is_valid():
           obj = form.save()
           obj.Patient =Patient.objects.get(id=request.session["Patient_id"])
           obj.save()
           return redirect('pat_health_rec_list_create')
    else:
        form = PatHealthRecForm()
    pat_health_recs = PatHealthRec.objects.all()
    return render(request, 'pat_health_rec_list_create.html', {'form': form, 'pat_health_recs': pat_health_recs})

def pat_health_rec_edit(request, pk):
    pat_health_rec = get_object_or_404(PatHealthRec, pk=pk)
    if request.method == 'POST':
        form = PatHealthRecForm(request.POST, instance=pat_health_rec)
        if form.is_valid():
            form.save()
            return redirect('pat_health_rec_list_create')
    else:
        form = PatHealthRecForm(instance=pat_health_rec)
    return render(request, 'pat_health_rec_edit.html', {'form': form})

def pat_health_rec_delete(request, pk):
    pat_health_rec = get_object_or_404(PatHealthRec, pk=pk)
    if request.method == 'POST':
        pat_health_rec.delete()
        return redirect('pat_health_rec_list_create')
    return render(request, 'pat_health_rec_delete.html', {'pat_health_rec': pat_health_rec})

# ApplyScan
def apply_scan_list_create(request):
    if request.method == 'POST':
        form = ApplyScanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apply_scan_list_create')
    else:
        form = ApplyScanForm()
    apply_scans = ApplyScan.objects.all()
    return render(request, 'apply_scan_list_create.html', {'form': form, 'apply_scans': apply_scans})

def apply_scan_edit(request, pk):
    apply_scan = get_object_or_404(ApplyScan, pk=pk)
    if request.method == 'POST':
        form = ApplyScanForm(request.POST, instance=apply_scan)
        if form.is_valid():
            form.save()
            return redirect('apply_scan_list_create')
    else:
        form = ApplyScanForm(instance=apply_scan)
    return render(request, 'apply_scan_edit.html', {'form': form})

def apply_scan_delete(request, pk):
    apply_scan = get_object_or_404(ApplyScan, pk=pk)
    if request.method == 'POST':
        apply_scan.delete()
        return redirect('apply_scan_list_create')
    return render(request, 'apply_scan_delete.html', {'apply_scan': apply_scan})

# CounsellingBook
def counselling_book_list_create(request):
    if request.method == 'POST':
        booking_date = request.POST.get("booking_date")
        time_slot = request.POST.get("time_slot")
        patid = request.session["Patient_id"]
        pid = Patient.objects.get(id=patid)

        obj = CounsellingBook.objects.create(
            patientId=pid,
            Booking_date=booking_date,
            Times_lot=time_slot,
        )
        return redirect('counselling_book_list_create')
    else:
        form = CounsellingBookForm()
    counselling_books = CounsellingBook.objects.filter(patientId=request.session["Patient_id"])
    return render(request, 'counselling_book_list_create.html', {'form': form, 'counselling_books': counselling_books})

def counselling_book_edit(request, pk):
    counselling_book = get_object_or_404(CounsellingBook, pk=pk)
    if request.method == 'POST':
        form = CounsellingBookForm(request.POST, instance=counselling_book)
        if form.is_valid():
            form.save()
            return redirect('counselling_book_list_create')
    else:
        form = CounsellingBookForm(instance=counselling_book)
    return render(request, 'counselling_book_edit.html', {'form': form})

def counselling_book_delete(request, pk):
    counselling_book = get_object_or_404(CounsellingBook, pk=pk)
    if request.method == 'POST':
        counselling_book.delete()
        return redirect('counselling_book_list_create')
    return render(request, 'counselling_book_delete.html', {'counselling_book': counselling_book})

# RegFreevig
def reg_freevig_list_create(request):
    if request.method == 'POST':
        form = RegFreevigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reg_freevig_list_create')
    else:
        form = RegFreevigForm()
    reg_freevigs = RegFreevig.objects.all()
    return render(request, 'reg_freevig_list_create.html', {'form': form, 'reg_freevigs': reg_freevigs})

def reg_freevig_edit(request, pk):
    reg_freevig = get_object_or_404(RegFreevig, pk=pk)
    if request.method == 'POST':
        form = RegFreevigForm(request.POST, instance=reg_freevig)
        if form.is_valid():
            form.save()
            return redirect('reg_freevig_list_create')
    else:
        form = RegFreevigForm(instance=reg_freevig)
    return render(request, 'reg_freevig_edit.html', {'form': form})

def reg_freevig_delete(request, pk):
    reg_freevig = get_object_or_404(RegFreevig, pk=pk)
    if request.method == 'POST':
        reg_freevig.delete()
        return redirect('reg_freevig_list_create')
    return render(request, 'reg_freevig_delete.html', {'reg_freevig': reg_freevig})

# Comments
def comments_list_create(request):
    if request.method == 'POST':
        patid = request.session["Patient_id"]
        pid = Patient.objects.get(id=patid)
        form = CommentsForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.Patient = pid
            obj.save()
            return redirect('comments_list_create')
    else:
        form = CommentsForm()

    comments = Comments.objects.all()
    return render(request, 'comments_list_create.html', {'form': form, 'comments': comments})


def comments_edit(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    if request.method == 'POST':
        form = CommentsForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comments_list_create')
    else:
        form = CommentsForm(instance=comment)
    return render(request, 'comments_edit.html', {'form': form})

def comments_delete(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('comments_list_create')
    return render(request, 'comments_delete.html', {'comment': comment})


# Search Scan Center
def search_scan_center(request):
    context = {}
    form = District(request.POST or None, request.FILES or None)
    if request.POST:
        dist = request.POST.get('District')
        context["dataset"] = ScanCenter.objects.filter(District=dist)
        context["frm"] = form
        return render(request, "search_scan_center.html", context)
    context["frm"] = form
    return render(request, 'search_scan_center.html',context)


def scan_type_view(request,scnid):
    dataset = ScanType.objects.all()
    selected_items = []
    total = 0

    if request.method == "POST":
        selected_ids = request.POST.getlist("scans")
        selected_items = []
        print("cal scan IDs:", selected_ids)
        for item in ScanType.objects.filter(id__in=selected_ids):
            final_price = item.Amount - item.Discount
            selected_items.append({
                "name": item.Scan_Type,
                "amount": item.Amount,
                "discount": item.Discount,
                "final": final_price,
                "selected_ids":selected_ids

            })
            total += final_price

    context = {
        "dataset": dataset,
        "selected_items": selected_items,
        "total": total,
        "scanningcnre":scnid,

    }
    return render(request, 'scan_type_View.html', context)


def getAppointment(request):
    if request.method == "POST":
        booking_date = request.POST.get("bkdate")
        time_slot = request.POST.get("Slot")
        patid = request.session["Patient_id"]
        pid = Patient.objects.get(id=patid)
        scan_ids_str = request.POST.getlist("scans")

        # Convert scan_ids from strings to integers
        scan_ids = [int(sid) for sid in scan_ids_str]
        center_id = request.POST.get("ctr")
        amount = request.POST.get("amount")
        print("Selected scan IDs:", scan_ids)
        print(center_id)

        existing_slot_count = ApplyScan.objects.filter(
            Booking_Date=booking_date,
            Preferred_time=time_slot
        ).count()

        if existing_slot_count >= 5:
            return HttpResponse(
                "<script>"
                "alert('This time slot is full. Please choose another time slot and date.');"
                "window.history.back();"
                "</script>"
            )

        daily_count = ApplyScan.objects.filter(Booking_Date=booking_date).count()

        obj = ApplyScan.objects.create(
            patient=pid,
            Scan_Center=ScanCenter.objects.get(id=center_id),
            Booking_Date=booking_date,
            Preferred_time=time_slot,
            Amount=amount,
        )
        obj.Scan_Type.set(scan_ids)
        obj.Coupon = daily_count + 1
        obj.save()

        past_appointments = ApplyScan.objects.filter(patient=pid).exclude(id=obj.id).order_by('-Booking_Date')

        context = {
            'appointment': obj,
            'past_appointments': past_appointments,
        }

        return render(request, 'Appointment.html', context)



def guidelines_patient_view(request):
    context={}
    context['dataset']= GuideLines.objects.all()
    return render(request, 'guidlines_patient.html',context)