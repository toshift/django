# coding: utf-8

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bootstview.models import Book
from bootstview.forms import BookForm


def book_list(request):
    """"書籍の一覧"""
#    return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render(request,
                  'bootstview/book_list.html',    # 使用するテンプレート
                  {'books': books})               # テンプレートに渡すデータ

def book_edit(request, book_id=None):
    """書籍の編集"""
#    return HttpResponse('書籍の編集')

    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()
    
    if request.method == 'POST': # POSTされたrequestでーたからフォームを作成
        form = BookForm(request.POST, instance=book)
        if form.is_valid():    # フォームのバリデーション
            book = form.save(commit=False)
            book.save()
            return redirect('bootstview:book_list')
    else: # GETの時
        form = BookForm(instance=book)    # book インスタンスからフォームを作成
    return render(request, 'bootstview/book_edit.html', dict(form=form, book_id=book_id))


def book_del(request, book_id):
    """書籍の削除"""
#    return HttpResponse('書籍の削除')
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('bootstview:book_list')

