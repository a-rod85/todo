from django.shortcuts import render

# Create your views here.
def Get_todo_list(request):
    return render(request, 'todo/todo_list.html')