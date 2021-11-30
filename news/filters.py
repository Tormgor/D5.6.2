from django_filters import FilterSet, DateRangeFilter
from .models import Article

class ArticleFilter(FilterSet):
    datetime = DateRangeFilter
    class Meta:
        model = Article
        fields = {'title': ['icontains'],
                  'author': ['exact'],
                  'datetime': ['gt']}

