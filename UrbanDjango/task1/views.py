from django.shortcuts import render
from django.http import HttpResponse
from task1.forms import UserRegister
from task1.models import Buyer, Game
# Create your views here.
def main_page(request):
    title = "Главная страница"
    link1 = "Главная"
    link2 = "Магазин"
    link3 = 'Корзина'
    context = {'title':title, 'link1':link1,'link2':link2, 'link3':link3}
    return render(request,'platform.html', context)

def store(request):
    title = 'Ассортимент'
    buy = 'Купить'
    games = Game.objects.all()
    back = 'Вернуться обратно'
    context={'title':title, "buy":buy, 'games':games, 'back':back}
    return render(request,'games.html', context)

def korzina(request):
    title = 'Корзина'
    back = 'Вернуться обратно'
    context={'title':title, 'back':back}
    return render(request,'cart.html', context)



def sign_up_by_django(request):
    Users = Buyer.objects.all()
    usernames = [i.name for i in Users]
    info = {'error':[]}
    i = 0
    form = UserRegister(request.POST)
    if request.method =="POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeate_password = form.cleaned_data['repeate_password']
            age = form.cleaned_data['age']
            if username not in usernames and password == repeate_password and int(age) >= 18:     
                Buyer.objects.create(name=username, age=age)   
                context = {'username':username}           
                return render(request, 'registration_complite.html', context)
            elif username in usernames:    
                i +=1
                info[f'error {i}'] = HttpResponse('Этот логин уже занят', status=400, reason='repeated login') 
                print(info[f'error {i}'])   
                return HttpResponse('Этот логин уже занят', status=400, reason='repeated login')    
            elif password != repeate_password:
                password_no = True
                i +=1
                info[f'error {i}'] = HttpResponse('Этот логин уже занят', status=400, reason='repeated login') 
                print(info[f'error {i}'])   
                return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            elif int(age) < 18:
                age_no = True
                i +=1
                info[f'error {i}'] = HttpResponse(f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18-int(age)} лет', status=400, reason='insufficient age')
                return HttpResponse(f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18-int(age)} лет', status=400, reason='insufficient age')
    else:
        
        form = UserRegister()
        context = {'info':info, 'form':form}
        return render(request, 'registration_page.html', context)