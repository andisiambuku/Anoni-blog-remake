from django.shortcuts import render


posts= [
    {
        'author':'Backend Dev',
        'title' : 'Hello Server',
        'content' : 'Lorem ipsummmmmm',
        'date_posted' : 'August 29,2031'
    },
    {
        'author':'Frontend Dev',
        'title' : 'Hello World',
        'content' : 'Lorem ipsummmmmm',
        'date_posted' : 'August 30,2031'
    }
]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})