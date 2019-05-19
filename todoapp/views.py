from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from todoapp.models import Todo
from todoapp import utils
import datetime
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class Dashboard(View):

    def get(self, request):
        return render(request, 'index.html',)
 
    def post(self, request):
        data = eval(request.body)
        if data.get('method') == 'delete':
            obj =Todo.objects.get(pk = data.get('deleteId'))
            obj.visible_status = False
            obj.save()
            record_list =  utils.gettodolist()
            return JsonResponse({"data":record_list,"status":"delete successfully"})
        
        elif data.get('method') == 'save_rec':
            yr, mnth, day = data.get('completion_date').split('-')
            dateobj = datetime.datetime(year= int(yr), month= int(mnth), day= int(day))
            if data.get("edit_id") == 'true':
                Todo.objects.filter(pk= data.get("edit_id")).update(title= data.get('title'),Descriptions = data.get("descriptions"), completion_date=dateobj, status=data.get('status'), visible_status= True)
            else:
                obj = Todo(title= data.get('title'),Descriptions = data.get("descriptions"), completion_date=dateobj, status=data.get('status'), visible_status= True)
                obj.save()

            record_list =  utils.gettodolist()
            return JsonResponse({"data":record_list, "status":"saved successfully"})


def gettodolist(request):
    record_list =  utils.gettodolist()
    return JsonResponse({"data":record_list})

