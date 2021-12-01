from django.shortcuts import redirect, render
from .models import Topic
from .forms import TopicForm
from .forms import EntryForm

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


def new_entry(request,topic_id):           #******* interview q - url.py file has a variable called topic_id, so we must use the same variable
                                           #or else the website will crash
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
                                                #form we're creating only gives the text field, date_added field from models is automatically generated
        if form.is_valid():
            new_entry = form.save(commit=False) #tells database we're not ready to write to it yet
            new_entry.topic = topic             #assigns entry to a topic
            new_entry.save()

            return redirect('MainApp:topic',topic_id=topic_id)

    context = {'form': form, 'topic':topic}
    return render(request, 'MainApp/new_entry.html', context)