from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Profile
from .forms import ProfileForm

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

def profile_create(request):
    data = dict()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            profiles = Profile.objects.all()
            data['html_profile_list'] = render_to_string('profiles/includes/partial_profile_list.html', {
                'profiles': profiles
            })
        else:
            data['form_is_valid'] = False
    else:
        form = ProfileForm()

    context = {'form': form}
    data['html_form'] = render_to_string('profiles/includes/partial_profile_create.html',
        context,
        request=request
    )
    return JsonResponse(data)