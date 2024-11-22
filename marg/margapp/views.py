from django.shortcuts import render, redirect
from .forms import UserDataForm
from .models import UserData

# View to display the form
def input_form(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            # Redirect to the page that displays the stored data
            return redirect('show_data')

    else:
        form = UserDataForm()

    return render(request, 'index.html', {'form': form})

# View to show all stored data
def show_data(request):
    # Fetch all data from the database
    data = UserData.objects.all()

    return render(request, 'show_data.html', {'data': data})
