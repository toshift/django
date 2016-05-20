# coding: utf-8
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from django.shortcuts import(
    render,
    redirect,
)
from .models import Posting
from .forms import PostingForm
from django.contrib import messages

def _get_page(list_, page_no, count=5):
    """ページネータを使い、表示するページ情報を取得する"""
    paginator = Paginator(list_, count)
    try:
        page = paginator.page(page_no)
    except (EmptyPage, PageNotAnInteger):
        # page_noが指定されていない場合、数値がない場合、範囲外の場合は
        # 先頭のページを表示する
        page = paginator.page(1)
    return page

def index(request):
    """表示・登校を処理する"""
    # ModelFormもFormもインスタンスを作るタイミングでの使い方は同じ
    form = PostingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # save()メソッドを呼ぶだけでModelを使ってDBに登録される。
            form.save()
            # メッセージフレームワークを使い、処理が成功したことをユーザーに通知する。
            messages.success(request, '投稿を受付けました。')
            return redirect('guestboard:index')
        else:
            # メッセージフレームワークを使い、処理が失敗したことをユーザーに通知する。
            messages.error(request, '入力内容に誤りがあります。')
    page = _get_page(
        Posting.objects.order_by('-id'), # 投稿を新しい順に並び替えて取得する
        request.GET.get('page') # GETクエリからページ番号を取得する
    )
    contexts = {
        'form': form,
        'page': page,
    }
    return render(request, 'guestboard/index.html', contexts)

