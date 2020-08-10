from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, EmployeeUpdateForm, MemberRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Member


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'persons/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = EmployeeUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.employee)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = EmployeeUpdateForm(instance=request.user.employee)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'persons/profile.html', context)

def create_member(request):
    if request.method == 'POST':
        print("debug Line 1")
        print(request.POST)
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            ssn = form.cleaned_data.get('ssn')
            firstName = form.cleaned_data.get('firstName')
            middleName = form.cleaned_data.get('middleName')
            lastName = form.cleaned_data.get('lastName')
            diagnosis = form.cleaned_data.get('diagnosis')
            member = Member(ssn=ssn, firstName=firstName, middleName=middleName, lastName=lastName, diagnosis=diagnosis)
            member.save()
            messages.success(request, f'New Member {firstName} {lastName} has been created!')
            return redirect('logsheet-home')
            
        else:
            return redirect('login')
    else:
        form = MemberRegistrationForm()

    return render(request, 'persons/create_member.html', {'form': form})
 


 
