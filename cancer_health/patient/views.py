from django.shortcuts import render, redirect, get_object_or_404
from .models import PatHealthRec, ApplyScan, CounsellingBook, RegFreevig, Comments
from .forms import PatHealthRecForm, ApplyScanForm, CounsellingBookForm, RegFreevigForm, CommentsForm

# PatHealthRec
def pat_health_rec_list_create(request):
    if request.method == 'POST':
        form = PatHealthRecForm(request.POST)
        if form.is_valid():
            form.save()
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
        form = CounsellingBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('counselling_book_list_create')
    else:
        form = CounsellingBookForm()
    counselling_books = CounsellingBook.objects.all()
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
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
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