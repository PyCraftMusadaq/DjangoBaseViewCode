from django.shortcuts import render
from django.views import View 
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic.detail import DetailView
from .models import Student
# Create your views here.

class MyclassView1(View):
    def get(self,request):
        return render(request,"home.html")
        
    
class MyclassView2(View):
    name = "Musadaq"
    def get(self,request):
        return render(request,"home.html",{'name':self.name})
    def post(self,request):
        data = request.POST.get('name')
        print(data)
        return render(request,"home.html",{'name':"Data Saved Sucessfully"})
    def put(self,request):
        name = request.POST.get('name')
        print(name)
        return 
    def delete(self,request):
        name = request.POST.get('name')
        print(name)
        return 
    
    
# Template View To render template. it is just basically used we can render it from url also 
# to render the context data from backend to frontend we will use get_context_data 
class HomePageView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs) # it is used to get parent's context and then add our own data and render back it to frontend .
        # If you want to pass extra _context from url to this view you can use extra_context argument in view. visit url for complete information. 
        context['student'] = "Musadaq"
        context['role'] = 'tenat'
        return context 
    

# Profile page with dynamic passing values 
class ProfilePageView(TemplateView):
    template_name = "profile.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['name'] = "Musadaq Tanveer"
        print(kwargs['id']) # passed keyword argument can also been seen in this view 
        return context 
    


class MyDefaultView(RedirectView):
    url = 'home'
    #pattern_name = 'home'
    query_string = True # if we want to get query parameters passed in url 
    # url = 'https://google.com  # external urls can also be used 
    # one of them can be use to redirect from this view to target view 
    # if we want to pass arguments in url then we can use get_redirect_url function and extract **kwargs
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)
    
# Base View for single details    
class SingleStudentView(View):
    def get(self,request,pk):
        single_student = Student.objects.get(pk=pk)
        return render(request,"profile.html",{'student':single_student})
      
# Detail View
class StudentDetailView(DetailView):
    # model from we are getting detail of instance
    model = Student
    template_name = 'profile.html'
    # if we change the slug from pk to another we will use pk_url_kwarg
    #pk_url_kwarg = 'id' # 
    #template_name_suffix = "_detail"
    # context name is same as model name like student in our case but if we want to chang we can as usual we did 
    context_object_name = 'student'
    # if we want to pass aditional data we can use this method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['musadaq'] = Student.objects.all().order_by('name')
        return context 
        
            