# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from bootstview.models import Book


def book_list(request):
    """"書籍の一覧"""
#    return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render(request,
                  'bootstview/book_list.html',    # 使用するテンプレート
                  {'books': books})               # テンプレートに渡すデータ

def book_edit(request, book_id=None):
    """書籍の編集"""
    return HttpResponse('書籍の編集')


def book_del(request, book_id):
    """書籍の削除"""
    return HttpResponse('書籍の削除')
