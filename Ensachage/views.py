from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib import messages
from datetime import datetime, timedelta, date
from django.db.models import Sum, Avg, Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.

today = date.today()

tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
start_week = today - timedelta(today.weekday())
end_week = start_week + timedelta(days=7)

print(today, tomorrow, yesterday)




class list_View(View):
    template_name = "Products/list.html"
    
    def get_object(self):
        
        return EnsachageModel.objects.filter(Q(created__gte=today) & Q(created__lt=tomorrow))
    def get(self, request, *args, **kwargs):
        
        context={
            'obj': self.get_object().order_by('created', '-pk'),
            'liv_total': self.get_object().aggregate(liv=Sum('livraison')),
            'cas_total': self.get_object().aggregate(cas=Sum('casse')),
            'ens_total': self.get_object().aggregate(ens=Sum('ensache')),
            'tx_cas_total': self.get_object().aggregate(tx_cas=Avg('tx_casse')),
            'vra_total': self.get_object().aggregate(vra=Sum('vrack')), 
        }
        
        return render(request, self.template_name, context)
    
class detail_View(View):
    
    template_name = "Products/detail.html"
    
    def get_object(self, *args, **kwargs):
        user = self.kwargs.get('user', None)
        user = get_object_or_404(User, username=user)        
        return user
        
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        month = self.request.GET.get('month', None)
        year = self.request.GET.get('year', None)
        if user is not None :
            obj = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=today.month) & Q(created__year=today.year)).order_by('-created', '-pk')
            liv_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=today.month) & Q(created__year=today.year)).aggregate(liv=Sum('livraison'))
            cas_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=today.month) & Q(created__year=today.year)).aggregate(cas=Sum('casse'))
            ens_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=today.month) & Q(created__year=today.year)).aggregate(ens=Sum('ensache'))
            tx_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=today.month) & Q(created__year=today.year)).aggregate(tx=Avg('tx_casse'))
            vra_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=today.month) & Q(created__year=today.year)).aggregate(vra=Sum('vrack'))
        if user is not None and month is not None and year is not None:
            obj = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=month) & Q(created__year=year)).order_by('-created', '-pk')
            liv_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=month) & Q(created__year=year)).aggregate(liv=Sum('livraison'))
            cas_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=month) & Q(created__year=year)).aggregate(cas=Sum('casse'))
            ens_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=month) & Q(created__year=year)).aggregate(ens=Sum('ensache'))
            tx_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=month) & Q(created__year=year)).aggregate(tx=Avg('tx_casse'))
            vra_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__month=month) & Q(created__year=year)).aggregate(vra=Sum('vrack'))
        context={
            'month':month,
            'year':year,
            'obj': obj,
            'liv_total':liv_total,
            'cas_total':cas_total,
            'ens_total':ens_total,
            'tx_total':tx_total,
            'vra_total':vra_total,
        }
        return render(request, self.template_name, context)

class filter_year_View(View):
    template_name = 'Products/filter.html'
    
    def get_object(self):
        user = self.kwargs.get('user', None)
        user = get_object_or_404(User, username=user)
        return user
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        year = request.GET.get('year', None)
        
        if user is not None:
            obj = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=today.year)).order_by('-created')
            liv_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=today.year)).aggregate(liv=Sum('livraison'))
            cas_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=today.year)).aggregate(cas=Sum('casse'))
            ens_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=today.year)).aggregate(ens=Sum('ensache'))
            tx_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=today.year)).aggregate(tx=Avg('tx_casse'))
            vra_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=today.year)).aggregate(vra=Sum('vrack'))
        if user is not None and year is not None:
            obj = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=year)).order_by('-created')
            liv_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=year)).aggregate(liv=Sum('livraison'))
            cas_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=year)).aggregate(cas=Sum('casse'))
            ens_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=year)).aggregate(ens=Sum('ensache'))
            tx_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=year)).aggregate(tx=Avg('tx_casse'))
            vra_total = EnsachageModel.objects.filter(Q(user=user.pk) & Q(created__year=year)).aggregate(vra=Sum('vrack'))
            
        context = {
            'year':year,
            'obj': obj,
            'liv_total':liv_total,
            'cas_total':cas_total,
            'ens_total':ens_total,
            'tx_total':tx_total,
            'vra_total':vra_total,
        }
        return render(request, self.template_name, context)

class yesterday_View(View):
    template_name = 'Products/yesterday_view.html'
    
    def get_object(self):
        return EnsachageModel.objects.filter(Q(created=yesterday))
    
    def get(self, request, *args, **kwargs):
        context={
            'obj': self.get_object().order_by('-created'),
            'liv_total': self.get_object().aggregate(liv=Sum('livraison')),
            'cas_total': self.get_object().aggregate(cas=Sum('casse')),
            'ens_total': self.get_object().aggregate(ens=Sum('ensache')),
            'tx_total': self.get_object().aggregate(tx=Avg('tx_casse')),
            'vra_total': self.get_object().aggregate(vra=Sum('vrack')),
        }
        return render(request, self.template_name, context)

class week_View(View):
    template_name = 'Products/week_view.html'
    
    def get_object(self):
        return EnsachageModel.objects.filter(Q(created__range=[start_week, end_week]))
    def get(self, request, *args, **kwargs):
        context = {
            'obj':self.get_object().order_by('-created'),
            'liv_total':self.get_object().aggregate(liv=Sum('livraison')),
            'cas_total':self.get_object().aggregate(cas=Sum('casse')),
            'ens_total':self.get_object().aggregate(ens=Sum('ensache')),
            'tx_total':self.get_object().aggregate(tx=Avg('tx_casse')),
            'vra_total':self.get_object().aggregate(vra=Sum('vrack')),
        }
        return render(request, self.template_name, context)
class month_View(View):
    template_name = 'Products/month_view.html'
    
    def get_object(self):
        return EnsachageModel.objects.filter(Q(created__month=today.month) & Q(created__year=today.year))
    
    def get(self, request, *args, **kwargs):
        context={
            'obj': self.get_object().order_by('-created'),
            'liv_total': self.get_object().aggregate(liv=Sum('livraison')),
            'cas_total': self.get_object().aggregate(cas=Sum('casse')),
            'ens_total': self.get_object().aggregate(ens=Sum('ensache')),
            'tx_total': self.get_object().aggregate(tx=Avg('tx_casse')),
            'vra_total': self.get_object().aggregate(vra=Sum('vrack')),
        }
        return render(request, self.template_name, context)
    
class year_View(View):
    template_name = 'Products/year_view.html'
    
    def get_object(self):
        return EnsachageModel.objects.filter(created__year=today.year)
    
    def get(self, request, *args, **kwargs):
        context={
            'obj': self.get_object().order_by('-created'),
            'liv_total': self.get_object().aggregate(liv=Sum('livraison')),
            'cas_total': self.get_object().aggregate(cas=Sum('casse')),
            'ens_total': self.get_object().aggregate(ens=Sum('ensache')),
            'tx_total': self.get_object().aggregate(tx=Avg('tx_casse')),
            'vra_total': self.get_object().aggregate(vra=Sum('vrack')),
        }
        return render(request, self.template_name, context)
    
    
class create_View(View):
    template_name = 'Products/create.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,)
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user = request.POST.get('user', None)
            liv = int(request.POST.get('liv', None))
            cas = int(request.POST.get('cas', None))
            vra = float(request.POST.get('vra', None).replace(',','.'))
            date = request.POST.get('date', None).replace('/', '-')
            
            user = get_object_or_404(User, username=user)
            print(user)
            
            obj = EnsachageModel.objects.create(
                user=user,
                livraison=liv,
                casse=cas,
                vrack=vra,
                created=date,
            )
            
            if obj is not None:
                obj.save()
                return redirect('list')
            
        return render(request, self.template_name, {'obj':obj} )
    
class update_View(View):
    template_name = 'Products/update.html'
    
    def get_object(self):
        pk = self.kwargs.get('pk', None)
        print(pk)
        if pk is not None:
            obj = get_object_or_404(EnsachageModel, pk=pk)
        return obj
        
    def get(self, request, *args, **kwargs):
        
        context={
            'obj':self.get_object()
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if request.method == 'POST':
            user = request.POST.get('user', None)
            liv = int(request.POST.get('liv', None))
            cas = int(request.POST.get('cas', None))
            vra = float(request.POST.get('vra', None).replace(',','.'))
            date = request.POST.get('date', None).replace('/', '-')
            
            ens = liv * 20
            tx = round((cas * 100)/(ens + cas), 2)
            
            user = get_object_or_404(User,username=user)
            print(user.pk)
            if user is not None:
                obj = EnsachageModel.objects.filter(pk=pk)
                obj = obj.update(
                    user=user.pk,
                    livraison=liv,
                    casse=cas,
                    ensache=ens,
                    tx_casse=tx,
                    vrack=vra,
                    created=date,
                )
                return redirect('details', user=user)
        return render(request, self.template_name, {'obj': obj})
    
class delete_View(View):
    template_name = 'Products/delete.html'
    
    def get_object(self):
        pk =self.kwargs.get('pk', None)
        
        return get_object_or_404(EnsachageModel, pk=pk)
    
    def get(self, request, *args, **kwargs):
        
        context={
            'obj':self.get_object(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user = self.get_object().user
        user = get_object_or_404(User, username=user)
        print(user)
        
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            return redirect('details', user=user)
        return render(request, self.template_name, {'obj': obj})
    
class admin_View(View):
    template_name = 'Products/admin_list.html'
    def get_object(self):
        return EnsachageModel.objects.all()
    def get(self, request, *args, **kwargs):
        
        qu= request.GET.get('qu', None)
        qd = request.GET.get('qd', None)
        print(qu, qd)
        obj = self.get_object().order_by('-created', '-pk')
        liv_total = self.get_object().aggregate(liv=Sum('livraison'))
        cas_total = self.get_object().aggregate(cas=Sum('casse'))
        ens_total = self.get_object().aggregate(ens=Sum('ensache'))
        tx_total = self.get_object().aggregate(tx=Avg('tx_casse'))
        vra_total = self.get_object().aggregate(vra=Sum('vrack'))
        
        
        if qu and qd:
            obj = EnsachageModel.objects.filter(Q(user__username__icontains=qu) & Q(created__year__icontains=qd)).order_by('-created', '-pk')
            liv_total = EnsachageModel.objects.filter(Q(user__username__icontains=qu) & Q(created__year__icontains=qd)).aggregate(liv=Sum('livraison'))
            cas_total = EnsachageModel.objects.filter(Q(user__username__icontains=qu) & Q(created__year__icontains=qd)).aggregate(cas=Sum('casse'))
            ens_total = EnsachageModel.objects.filter(Q(user__username__icontains=qu) & Q(created__year__icontains=qd)).aggregate(ens=Sum('ensache'))
            tx_total = EnsachageModel.objects.filter(Q(user__username__icontains=qu) & Q(created__year__icontains=qd)).aggregate(tx=Avg('tx_casse'))
            vra_total = EnsachageModel.objects.filter(Q(user__username__icontains=qu) & Q(created__year__icontains=qd)).aggregate(vra=Sum('vrack'))
        context = {
            'obj':obj,
            'qu':qu,
            'qd':qd,
            'liv_total': liv_total,
            'cas_total': cas_total,
            'ens_total': ens_total,
            'tx_total': tx_total,
            'vra_total': vra_total,
        }
        return render(request, self.template_name, context)

class admin_update_View(View):
    template_name = 'Products/admin_update.html'
    
    def get_object(self):
        pk = self.kwargs.get('pk', None)
        print(pk)
        if pk is not None:
            obj = get_object_or_404(EnsachageModel, pk=pk)
        return obj
        
    def get(self, request, *args, **kwargs):
        
        context={
            'obj':self.get_object()
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if request.method == 'POST':
            user = request.POST.get('user', None)
            liv = int(request.POST.get('liv', None))
            cas = int(request.POST.get('cas', None))
            vra = float(request.POST.get('vra', None).replace(',','.'))
            date = request.POST.get('date', None).replace('/', '-')
            
            ens = liv * 20
            tx = round((cas * 100)/(ens + cas), 2)
            
            user = get_object_or_404(User,username=user)
            print(user.pk)
            if user is not None:
                obj = EnsachageModel.objects.filter(pk=pk)
                obj = obj.update(
                    user=user.pk,
                    livraison=liv,
                    casse=cas,
                    ensache=ens,
                    tx_casse=tx,
                    vrack=vra,
                    created=date,
                )
                return redirect('admin_view')
        return render(request, self.template_name, {'obj': obj})
    
class admin_delete_View(View):
    template_name = 'Products/admin_delete.html'
  
    def get_object(self):
        pk =self.kwargs.get('pk', None)
        
        return get_object_or_404(EnsachageModel, pk=pk)
    
    def get(self, request, *args, **kwargs):
        
        context={
            'obj':self.get_object(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user = self.get_object().user
        user = get_object_or_404(User, username=user)
        print(user)
        
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            return redirect('admin_view')
        return render(request, self.template_name, {'obj': obj})
        