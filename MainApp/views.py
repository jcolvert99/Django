from django.shortcuts import redirect, render
from .models import Topic
from .forms import TopicForm

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


def topic(request,topic_id):     #what you name in url file must be received in views file
    topic = Topic.objects.get(id=topic_id)

    entries = topic.entry_set.all()        #from myshell.py file

    context = {'topic':topic, 'entries':entries}  #key represents a variable name to use in template
                                                  #value reprsents a variable name to use in views
    return render(request, 'MainApp/topic.html',context)



def new_topic(request):
    if request.method != 'POST':    #if get request
        form = TopicForm()          #loads an empty form
    else:
        form = TopicForm(date=request.POST)  #if post request, take data from webpage and save it in form

        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')

    context = {'form':form}         #interview q- context is a dict that allows us to pass data to the html file
    return render(request, 'MainApp/new_topic.html',context)