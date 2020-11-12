from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../test')


def user_login(request):
    master_genes = Gene.objects.all()
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('../test')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'genedata/login.html', {'master_genes': master_genes})


def register(request):
    master_genes = Gene.objects.all()

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'organisation' in user_form.cleaned_data:
                profile.organisation = request.DATA['organisation']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'genedata/register.html',
                  {'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered, 'master_genes': master_genes})

def SPA(request):
    return render(request, 'genedata/spa.html')

class GeneList(ListView):
    model = Gene
    context_object_name = 'master_genes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        if "poslist" in self.request.get_full_path():
            context['genes'] = Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+')
        if 'type' in self.kwargs:
            if "Chromosome" in self.kwargs['type'] or "Plasmid" in self.kwargs['type']:
                context['genes'] = Gene.objects.filter(entity__exact=self.kwargs['type'])
        return context

    def get_template_names(self):
        if "poslist" in self.request.get_full_path():
             return 'genedata/list.html'
        if 'type' in self.kwargs:
            if "Chromosome" in self.kwargs['type'] or "Plasmid" in self.kwargs['type']:
                return 'genedata/list.html'

        return 'genedata/index.html'


class GeneDetail(DetailView):
    model = Gene
    context_object_name = 'gene'
    template_name = 'genedata/gene.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context


def poslist(request):
    genes = Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+')
    master_genes = Gene.objects.all()
    return render(request, 'genedata/list.html', {'genes': genes, 'type': 'PosList'})


class GeneDelete(DeleteView):
    model = Gene
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

class GeneUpdate(UpdateView):
    model = Gene
    fields = fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon',
              'sequencing', 'ec']
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

def create_ec(request):
    master_genes = Gene.objects.all()
    if request.method == 'POST':
        form = ECForm(request.POST)
        if form.is_valid():
            ec = EC()
            ec.ec_name = form.cleaned_data['ec_name']
            ec.save()
            return HttpResponseRedirect('/create_ec/')
    else:
        ecs = EC.objects.all()
        form = ECForm()
    return render(request, 'genedata/ec.html', {'form': form, 'ecs': ecs, 'master_genes': master_genes})


class GeneCreate(CreateView):
    model = Gene
    template_name = 'genedata/create_gene.html'
    form_class = GeneForm
    success_url = "/create_gene/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context
