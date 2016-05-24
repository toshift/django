from django.shortcuts import render

def starview(request):
    return render(request,
                  'starviews/starview.html'    # 使用するテンプレート
                 )               # テンプレートに渡すデータ
