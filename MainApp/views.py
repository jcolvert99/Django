from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    '''The home page for Learning Log'''
    return render(request, 'MainApp/index.html')


def topics(request):        #whatever you called it in urls must be the same
    topics = Topic.objects.order_by('date_added')  #calls the topics template
    
    context = {'topics':topics} #populating the template with the data
                                #using a DICTIONARY
                                    #key- variable used in the template file
                                    #value- variable used in the view function
    
    return render(request, 'MainApp/topics.html',context)