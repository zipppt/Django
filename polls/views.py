from django.http import HttpResponse

def index(request):
    if request.method == 'GET':
        return HttpResponse('Запрос получен')
    elif request.method == 'POST':
        return HttpResponse('Запрос опубликован')
