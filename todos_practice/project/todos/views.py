from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from users.models import User
from todos.models import Todo

# Create your views here.
'''
GET views
'''
def all_(request):
	if not request.GET.__contains__('token'):
		return HttpResponseNotFound(request)
	user = get_object_or_404(User, key_id=request.GET['token'])
	return JsonResponse({x.id:x.content for x in user.todo_set.all()})

def incomplete(request):
	if not request.GET.__contains__('token'):
		return HttpResponseNotFound(request)
	user = User.objects.get(key_id=request.GET['token'])
	return JsonResponse({x.id:x.content for x in user.todo_set.filter(finished=False)})

def date(request):
	if not request.GET.__contains__('token'):
		return HttpResponseNotFound(request)
	if not request.GET.__contains__('date'):
		return HttpResponseNotFound(request)
	user = User.objects.get(key_id=request.GET['token'])
	return JsonResponse({x.id:x.content for x in user.todo_set.filter(created_date=request.GET['date'])})

'''
POST views
'''
@csrf_exempt
def save_(request):
	if not request.POST.__contains__('token'):
		return HttpResponseNotFound(request)
	if not request.POST.__contains__('content'):
		return HttpResponseNotFound(request)
	user = get_object_or_404(User, key_id=request.POST['token'])
	todo = user.todo_set.create(content=request.POST['content'])
	return JsonResponse({todo.id: todo.content})

@csrf_exempt
def complete(request):
	if not request.POST.__contains__('token'):
		return HttpResponseNotFound(request)
	if not request.POST.__contains__('id'):
		return HttpResponseNotFound(request)
	user = get_object_or_404(User, key_id=request.POST['token'])
	todo = get_object_or_404(Todo, id=request.POST['id'])
	todo.finished = True
	todo.save()
	return JsonResponse({todo.id: todo.content})

@csrf_exempt
def update(request):
	if not request.POST.__contains__('token'):
		return HttpResponseNotFound(request)
	if not request.POST.__contains__('content'):
		return HttpResponseNotFound(request)
	if not request.POST.__contains__('id'):
		return HttpResponseNotFound(request)
	user = get_object_or_404(User, key_id=request.POST['token'])
	todo = user.todo_set.get(Todo, id=request.POST['id'])
	todo.content = request.POST['content']
	todo.save()
	return JsonResponse({todo.id: todo.content})

@csrf_exempt
def delete(request):
	if not request.POST.__contains__('token'):
		return HttpResponseNotFound(request)
	if not request.POST.__contains__('id'):
		return HttpResponseNotFound(request)
	user = get_object_or_404(User, key_id=request.POST['token'])
	todo = get_object_or_404(Todo, id=request.POST['id'])
	todo.delete()
	return JsonResponse({todo.id: todo.content})