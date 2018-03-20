from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from models import BlogArticles
def blog2_title   (request):
    blog2s = BlogArticles.objects.all()
    return render(request,'blog2/index.html',{"blog2s": blog2s})
def blog2_article(request, article_id):
    article = BlogArticles.objects.get(id =article_id)
    pub = article.publish
    return render(request,"blog2/content.html",{"article":article,"publish":pub })