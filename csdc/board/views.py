from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required , user_passes_test
from django.http import HttpResponseForbidden
from .models import Board , Comment
from .forms import BoardForm , CommentForm
from django.contrib import messages
from django.urls import reverse

# # Superuser 접근만 허용하는 데코레이터
# def superuser_required(view_func):
#     decorated_view_func = login_required(user_passes_test(lambda u: u.is_superuser)(view_func))
#     return decorated_view_func

def noticeBoard_list(request):
    boards = Board.objects.filter(type=0).order_by('-id')
    return render(request, 'boards/board_list.html' , {'boards': boards, 'notice': True})

def noticeBoard_detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'boards/board_detail.html', {'board': board, 'notice': True})

# 사용 예시
@login_required
def noticeBoard_create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.type = 0
            post.author = request.user.userprofile 
            post.created_date = timezone.now() 
            post.save()
            return redirect("board:noticeBoard_list") 
    else:
        form = BoardForm()
    return render(request, 'boards/board_create.html', {'form': form})

@login_required
def noticeBoard_update(request , board_id):
    post = get_object_or_404(Board, pk=board_id)  
    if request.method == "POST":
        form = BoardForm(request.POST, instance=post)  
        if form.is_valid():
            form.save()
            return redirect('board:noticeBoard_list')  
    else:
        form = BoardForm(instance=post)  
    
    return render(request, 'boards/board_update.html', {'form': form})

@login_required
def noticeBoard_delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if board.author.user != request.user:
        return HttpResponseForbidden()
    board.delete()
    return redirect('board:noticeBoard_list')

@login_required
def freeBoard_list(request):
    boards = Board.objects.filter(type=1).order_by('-id')
    return render(request, 'boards/board_list.html' , {'boards': boards})

@login_required
def freeBoard_detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.board = board
            comment.commenter = request.user.userprofile # 현재 로그인한 사용자
            print(comment.commenter)
            comment.save()
            return redirect('board:freeBoard_detail', board_id=board.id)
    else:
        comment_form = CommentForm()
    return render(request, 'boards/board_detail.html', {'board': board, 'comment_form': comment_form})

@login_required
def freeBoard_create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.userprofile
            post.created_date = timezone.now() 
            post.save()
            return redirect("board:freeBoard_list") 
    else:
        form = BoardForm()
    return render(request, 'boards/board_create.html', {'form': form})

@login_required
def freeBoard_update(request , board_id):
    post = get_object_or_404(Board, pk=board_id)  
    if request.method == "POST":
        form = BoardForm(request.POST, instance=post)  
        if form.is_valid():
            form.save()  
            return redirect('board:freeBoard_list')  
    else:
        form = BoardForm(instance=post)  
    
    return render(request, 'boards/board_update.html', {'form': form})

@login_required
def freeBoard_delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if board.author.user != request.user:
        return HttpResponseForbidden()
    board.delete()
    return redirect('board:freeBoard_list')

@login_required
def comment_delete(request, comment_id):
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)
        # 댓글 작성자만 삭제할 수 있도록 합니다.
        if request.user == comment.commenter.user or request.user.is_superuser:
            board_id = comment.board.id  # 댓글이 속한 게시글의 ID를 저장합니다.
            comment.delete()
            messages.success(request, '댓글이 성공적으로 삭제되었습니다.')
            return redirect(reverse('board:freeBoard_detail', args=[board_id]))
        else:
            messages.error(request, '댓글을 삭제할 권한이 없습니다.')
            return redirect(reverse('board:freeBoard_detail', args=[comment.board.id]))