from django.shortcuts import render,redirect
from .models import Message,Rooms,User
from django.http import JsonResponse
from .gemini_client import get_gemini_response
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,CustomUserChangeForm
# Create your views here.


@login_required(login_url='/login')
def home(request, room_id=None):
    user = request.user
    user_rooms = Rooms.objects.filter(host=user)
    user_messages = Message.objects.filter(user=user)

    room_messages = None
    selected_room = None
    

    if room_id:
        try:
          
            selected_room = Rooms.objects.get(id=room_id, host=user)
            room_messages = selected_room.message_set.all()
  
        except Rooms.DoesNotExist:
            messages.error(request, "Room not found.")
            return redirect('home') 

    context = {
        'user': user,
        'user_messages': user_messages,
        'rooms': user_rooms,
        'room_messages': room_messages,
        'selected_room': selected_room,
    }

    return render(request, 'bot/home.html', context)



@login_required(login_url='/login')
def chat_api(request,room_id=None):
    bot_response=""
    if request.method =='POST':
        user_input=request.POST.get('question')
        room = Rooms.objects.get(id=room_id)
        bot_response=get_gemini_response(user_input)
        
        user=request.user
        
        if user:
            Message.objects.create(user=user,room=room,sender='user',body=user_input)
            Message.objects.create( user=user,room=room,sender='bot',body=bot_response)
           
            return redirect('room',room_id=room.id)
        else:
            return JsonResponse({'Error':"invalid request method"},status=400)
        
        
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Email or password is incorrect!')
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist!')

    return render(request, 'bot/login.html')

 
def registerPage(request):
    
    form=CustomUserCreationForm()
    
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.username=user.username.lower()
            user.email=user.email.lower()
            user.save()
            login(request,user)
            return redirect('home')
        
        else:
            messages.error(request,'Please enter valid details...')
    
    context={'form':form}
    return render(request,'bot/register.html',context) 

def logoutPage(request):
    logout(request)
    return redirect('home')


@login_required(login_url='/login')
def create_room(request):
    if request.method == 'POST':
        name = request.POST.get('room_name')
        if name:
            new_room=Rooms.objects.create(name=name, host=request.user)
            return redirect('room', room_id=new_room.id)

    return redirect('home')




