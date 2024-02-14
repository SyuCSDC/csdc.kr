from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Board
from .forms import BoardForm
# Create your views here.
@login_required
def board_list(request):
    boards = Board.objects.all()
    return render(request, 'boards/board_list.html' , {'boards':boards})

@login_required
def board_detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'boards/board_detail.html', {'board': board})

@login_required
def board_create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.userprofile 
            post.created_date = timezone.now() 
            post.save()
            return redirect("board:board_list") 
    else:
        form = BoardForm()
    return render(request, 'boards/board_create.html', {'form': form})

@login_required
def board_update(request , board_id):
    post = get_object_or_404(Board, pk=board_id)  
    if request.method == "POST":
        form = BoardForm(request.POST, instance=post)  
        if form.is_valid():
            form.save()  
            return redirect('board:board_list')  
    else:
        form = BoardForm(instance=post)  
    
    return render(request, 'boards/board_update.html', {'form': form})

@login_required
def board_delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if board.author.user != request.user:
        return HttpResponseForbidden()
    board.delete()
    # 게시글 목록 페이지로 리다이렉트
    return redirect('board:board_list')