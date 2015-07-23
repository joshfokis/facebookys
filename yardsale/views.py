from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Followers, Warning
from .forms import AddWarningForm, FollowingForm, NewFollowerForm
# Create your views here.

def follower_list(request):
    names = Followers.objects.all()
    if request.method == "POST":
        form = NewFollowerForm(request.POST)
        form.save()
        return redirect('home')
    else:
        form = NewFollowerForm()
    return render(request, 'yardsale/followers_list.html', {'names': names, 'form':form})

def follower_warnings(request, pk):
    warn = get_object_or_404(Followers, pk=pk)
#     if request.method == "POST":
#         form = FollowingForm(request.POST, instance=warn)
#         fol = form.save(commit=False)
#         fol.following = warn.following
#         fol.save()
#         return redirect('yardsale.views.follower_warnings', pk=warn.pk)
#     else:
#         form = FollowingForm(instance=warn)
#         return render(request, 'yardsale/follower_warning.html', {'warn':warn, 'form':form})
    return render(request, 'yardsale/follower_warning.html', {'warn':warn})

def password_change_done(request):
    complete = "Your password has been changed."
    return render(request, 'registration/completed.html', {'complete':complete})

def follower_edit(request, pk):
    warn = get_object_or_404(Followers, pk=pk)
    if request.method == "POST":
        form = FollowingForm(request.POST, instance=warn)
        fol = form.save(commit=False)
        fol.following = warn.following
        fol.save()
        return redirect('yardsale.views.follower_warnings', pk=warn.pk)
    else:
        form = FollowingForm()
        return render(request, 'yardsale/follower_edit.html', {'warn':warn, 'form':form})

def new_warn(request, pk):
    print(pk)
    warn = get_object_or_404(Warning, pk=pk)
    fop = Followers.objects.get(pk=warn.person_id)
    if request.method == "POST":
        form = AddWarningForm(request.POST, request.FILES)
        if form.is_valid():
            postwarning = form.save(commit=False)
            postwarning.author = request.user
            postwarning.person = fop
            print(warn.person, warn, fop)
            print('pk ',warn.pk)
            postwarning.publish_date = timezone.now()
            postwarning.warn = warn
            print(postwarning.warn)
            postwarning.save()
            return redirect('yardsale.views.follower_warnings', pk=warn.pk)
    else:
        print(pk)
        form = AddWarningForm()
    return render(request, 'yardsale/addwarning.html', {'form':form})

def edit_warn(request, pk):
    warn = get_object_or_404(Warning, pk=pk)
    if request.method == "POST":
        form = AddWarningForm(request.POST, request.FILES, instance=warn)
        if form.is_valid():
            postwarning = form.save(commit=False)
            postwarning.person = warn.person
            postwarning.edited_date = timezone.now()
            postwarning.warn = warn
            postwarning.save()
            return redirect('yardsale.views.follower_warnings', pk=warn.pk)
    else:
        form = AddWarningForm(instance=warn)
    return render(request, 'yardsale/addwarning.html', {'form':form})

