from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

all_foods = [
    {'id':3,'title':'blue glacier','price':3999,'is_premium': False,'promotion_end_at': datetime(2022, 2, 28)},
    {'id':1,'title':'dark choco','price':4996,'is_premium': True,'promotion_end_at': datetime(2022, 2, 15)},
    {'id':2,'title':'red spicy','price':3999,'is_premium': False,'promotion_end_at': datetime(2022, 2, 15)},
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
