from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm
from .models import Story, StoryChapter, Interaction
from .forms import StoryForm, StoryChapterForm
from django.db.models import Count
from django.utils import timezone
from datetime import datetime



def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or any other page
    else:
        form = CustomLoginForm()

    return render(request, 'stories/login.html', {'form': form})


@login_required
def custom_logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout




@login_required
def create_story(request):
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            return redirect('add_chapter', pk=story.id)
    else:
        form = StoryForm()

    return render(request, 'stories/create_story.html', {'form': form})

@login_required
def add_chapter(request, pk):
    story = get_object_or_404(Story, id=pk)
    if request.method == "POST":
        form = StoryChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.story = story
            chapter.save()
            return redirect('add_chapter', pk=story.id)
    else:
        form = StoryChapterForm()
    
    return render(request, 'stories/add_chapter.html', {'form': form, 'story': story})





def read_story(request, pk, chapter_id=None):
    story = get_object_or_404(Story, id=pk)
    
    if chapter_id:
        current_node = get_object_or_404(StoryChapter, id=chapter_id)
    else:
        current_node = story.storychapter_set.first()

    next_parts = current_node.child_nodes.all()

    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        next_node = get_object_or_404(StoryChapter, id=choice_id)

        start_time_str = request.session.get('start_time', None)
        if start_time_str:
            start_time = datetime.fromisoformat(start_time_str)
        else:
            start_time = timezone.now()

        time_spent = timezone.now() - start_time

        Interaction.objects.create(
            user=request.user,
            story=story,
            current_node=next_node,
            time_spent=time_spent
        )

        request.session['start_time'] = timezone.now().isoformat()

        return redirect('read_chapter', pk=story.id, chapter_id=next_node.id)

    request.session['start_time'] = timezone.now().isoformat()

    return render(request, 'stories/read_story.html', {
        'story': story,
        'current_node': current_node,
        'next_parts': next_parts
    })








@login_required
def dashboard(request):
    stories = Story.objects.filter(author=request.user)

    total_reads = Interaction.objects.filter(story__author=request.user).count()

    popular_choices = (
        Interaction.objects.filter(story__author=request.user)
        .values('choice_made__content')
        .annotate(count=Count('choice_made'))
        .order_by('-count')[:5] 
    )

    time_tracking = (
        Interaction.objects.filter(story__author=request.user)
        .values('current_node__content')
        .annotate(avg_time_spent=Count('time_spent') / Count('current_node'))
        .order_by('-avg_time_spent')[:5]
    )

    completion_rate = (
        Interaction.objects.filter(story__author=request.user)
        .values('story')
        .annotate(completion_count=Count('current_node'))
    )

    context = {
        'stories': stories,
        'analytics': {
            'total_reads': total_reads,
            'popular_choices': popular_choices,
            'time_tracking': time_tracking,
            'completion_rate': completion_rate
        },
    }

    return render(request, 'stories/dashboard.html', context)
