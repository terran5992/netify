from django.shortcuts import render, redirect
from App import forms
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Record, Source



# Create your views here.

def index_view(request):

    if request.user.is_authenticated:

        try :
            user = User.objects.get(username = request.user)
        except:
            messages.error(request, "Unknown Error, Please Contact Admin")
            return redirect('index')

        sources = Source.objects.filter(user=user)
        source_name_list = []
        source_data_list = []

        for source in sources:
            source_name_list.append(source.name)
            source_data_list.append(int(source.records.latest().amount))
        

        context = {'sources':sources, 'src_name_list':source_name_list, 'src_data_list':source_data_list}

    else:
        context = {}
    return render(request, 'index.html', context)

def source_view(request,id):

    if request.user.is_authenticated:
        try :
            user = User.objects.get(username = request.user)
        except:
            messages.error(request, "Unknown Error, Please Contact Admin")
            return redirect('index')

        
        source = Source.objects.get(id=id)
        if source.user == user:
            print(source)
            src_labels = []
            src_amt = []

            for record in source.records.all():
                src_labels.append(record.date_added.strftime("%Y-%m-%d"))
                src_amt.append(int(record.amount))

            return render(request,'source_view.html',{'source':source, 'src_labels':src_labels, 'src_amt':src_amt})
        else:
            messages.error(request,'You are not authorized to view this source')
            return redirect('index')

    else:
        messages.danger(request,'You need to be logged in')
        return redirect('index')



def add_new_source(request):
    try :
        user = User.objects.get(username = request.user)
    except:
        messages.error(request, "Please Login To add to cart")
        return redirect('index')
    
    source_name = request.POST['source_name'] 
    amt = request.POST['amt'] 

    created_source = Source.objects.create(user = user, name = source_name)

    Record.objects.create(user = user, source = created_source, amount = amt)

    messages.success(request,'New Source Added ')
    return redirect('index')

def update_source(request):
    if request.method == "POST":
        if request.user.is_authenticated:

            try :
                user = User.objects.get(username = request.user)
            except:
                messages.error(request, "Unknown Error, Please Contact Admin")
                return redirect('index')

            source_id = request.POST['source_id']
            amt = request.POST['new_amt']

            source = Source.objects.get(id=source_id)

            record = Record.objects.create(user = user, source=source, amount = amt )

            messages.success(request, f"{source.name} has been updated to ${record.amount}")
            return redirect('index') 

        else:
            messages.danger('You need to be logged in')
            return redirect('index')
    else:
        messages.danger(request,'Wrong method used to enter this page')
        return redirect('index')

# TO TEST THE DELETE SOURCE BTN ( NOT TESTED YET )
def delete_source(request):
    if request.method == "POST":
        if request.user.is_authenticated:

            try :
                user = User.objects.get(username = request.user)
            except:
                messages.error(request, "Unknown Error, Please Contact Admin")
                return redirect('index')

            source_id = request.POST['source_id']

            Source.objects.get(id=source_id).delete()

            messages.info(request,'Source has been deleted')
            return redirect('index') 

        else:
            messages.error('You need to be logged in')
            return redirect('index')
    else:
        messages.error(request,'Wrong method used to enter this page')
        return redirect('index')

def logout_view(request):
    auth.logout(request)
    messages.info(request,"You have been logged out, See you soon!")
    return redirect('index')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user != None:
            auth.login(request,user)
            messages.success(request,'You have been logged in')
            return redirect('index')            
        else:
            messages.error(request,'Wrong credentials, please try again')
            return redirect('login')

        # auth and login user
    else:
        return render(request, 'login.html')

def signup_view(request):

    if request.method == "POST":
        form = forms.UserForm(request.POST)
        new_user = form.save()
        auth.login(request, new_user)
        messages.success(request,"Your account has been created and logged in !")
        return redirect('index')

    else:
        form = forms.UserCreationForm
        form2 = forms.UserForm

        return render(request, 'signup.html', {"form": form2})

def privacy_view(request):
    return render(request, 'privacy.html')