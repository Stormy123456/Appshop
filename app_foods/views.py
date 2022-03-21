from django.shortcuts import render
from django.http.response import HttpResponse

all_foods = [
    {'id':1,'title':'dark choco','price':499,'is_premium': True},
    {'id':2,'title':'red spicy','price':399,'is_premium': False},
    {'id':3,'title':'blue glacier','price':399,'is_premium': False},
]

# Create your views here.
def foods(request):
    context = {'foods':all_foods}
    return render(request,'app_foods/foods.html',context)

def food(request,food_id):
    one_food=None
    try:
        one_food = [f for f in all_foods if f['id'] == food_id][0]
    except IndexError:
        print('ไม่มีข้อมูล')
    context = {'food': one_food}
    return render(request,'app_foods/food.html', context)
