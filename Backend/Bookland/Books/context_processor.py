from .models import Category


def ContextCategory(request):
    return {'categories': Category.objects.all()}
