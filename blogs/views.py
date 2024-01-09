from django.shortcuts import redirect, render,get_object_or_404

from .models import Blog, Category

def posts_by_category(request, category_id):

    # Fetch the posts that belongs to the category with the id category_id
    posts= Blog.objects.filter(status='Published',category=category_id)

    # Use try/expect when we want to do some custom action if the category does not exists
    #try:
     # category=Category.objects.get(pk=category_id)

    #except:
     #  return redirect('home')
    
    # use get_object_404 whenyou want to show 404 error page if the category does not exist
    category=get_object_or_404(Category,pk=category_id)

    context={
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)
