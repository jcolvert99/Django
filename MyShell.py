import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all() #same as saying select * from in SQL- pulls all rows

for topic in topics:
    print(topic.id)         #called NoSQL
    print(topic.text)       # "." notation pulls the attributes in OOP
    print(topic.date_added)   #if you just pring topic then it will say "Topic Object 2" because hasn't processed the str function

t = Topic.objects.get(id=1)
print(t)

entries = t.entry_set.all()

for e in entries:
    print(e)