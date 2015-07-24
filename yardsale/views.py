from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.core.context_processors import csrf
from .models import Followers, Warning
from .forms import WarningForm, FollowingForm, FollowerForm
# Create your views here.

def follower_list(request):   
    args = {}
    args.update(csrf(request))
    args['names'] =Followers.objects.all().order_by('follower')
    args['form'] = FollowerForm() 
    if request.method == "POST":
        form = FollowerForm(request.POST)
        form.save()
        return redirect('home')
    else:
        form = FollowerForm()
    
    return render_to_response('yardsale/followers_list.html', args)

def follower_warnings(request, pk):
    warn = get_object_or_404(Followers, pk=pk)
    fop = get_object_or_404(Followers, pk=warn.pk)
    if request.method == "POST":
        form = FollowingForm(request.POST, instance=warn)
        fol = form.save(commit=False)
        fol.following = warn.following
        fol.save()
        return redirect('yardsale.views.follower_warnings', pk=fop.pk)
    else:
        form = FollowingForm(instance=warn)
    return render(request, 'yardsale/follower_warning.html', {'warn':warn, 'fop':fop, 'form':form})

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
    header = "<h2>Add Warning</h2>"
#     warn = get_object_or_404(Warning, pk=pk)
    fop = get_object_or_404(Followers, pk=pk)
    if request.method == "POST":
        form = WarningForm(request.POST, request.FILES)
        if form.is_valid():
            postwarning = form.save(commit=False)
            postwarning.author = request.user
            postwarning.person = fop
            postwarning.publish_date = timezone.now()
            postwarning.save()
            return redirect('yardsale.views.follower_warnings', pk=fop.pk)
    else:
        form = WarningForm()
    return render(request, 'yardsale/addwarning.html', {'form':form, 'fop':fop, 'header':header})

def edit_warn(request, pk):
    header = "<h2>Edit Warning</h2>"
    warn = get_object_or_404(Warning, pk=pk)
    if request.method == "POST":
        form = WarningForm(request.POST, request.FILES, instance=warn)
        if form.is_valid():
            postwarning = form.save(commit=False)
            postwarning.person = warn.person
            postwarning.edited_date = timezone.now()
            postwarning.warn = warn
            postwarning.save()
            return redirect('yardsale.views.follower_warnings', pk=warn.pk)
    else:
        form = WarningForm(instance=warn)
    return render(request, 'yardsale/addwarning.html', {'form':form, 'header':header})

def search_names(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
        if search_text is not None and search_text !=u"":
            search_text = request.POST['search_text']
            follower_list = Followers.objects.filter(follower__icontains=search_text)
            print(search_text)
        else:
            follower_list = []
        return render(request, 'yardsale/ajax_search.html', {'follower_list':follower_list})

