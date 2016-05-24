from django.shortcuts import render

def starview(request):
    return render(request, 'starviews/srarview.html', dict(form=form, book_id=book_id))