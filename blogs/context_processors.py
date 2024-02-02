from assingments.models import SocialLink
from .models import Category


def get_categories(request):
    categories= Category.objects.all()
    return dict(categories=categories)

def get_socaillinks(request):
    sociallinks=SocialLink.objects.all()
    return dict(sociallinks=sociallinks)