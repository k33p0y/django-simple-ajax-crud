from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from .models import Profile
from .forms import ProfileForm

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

def save_profile_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            profiles = Profile.objects.all()
            data['html_profile_list'] = render_to_string('profiles/includes/partial_profile_list.html', {
                'profiles': profiles
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
    else:
        form = ProfileForm()
    return save_profile_form(request, form, 'profiles/includes/partial_profile_create.html')

def profile_update(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
    else:
        form = ProfileForm(instance=profile)
    return save_profile_form(request, form, 'profiles/includes/partial_profile_update.html')