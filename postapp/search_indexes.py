#coding=utf-8
from haystack import indexes
from postapp.models import *
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text=indexes.CharField(document=True,use_template=True)
    title=indexes.NgramField(model_attr='title')
    content=indexes.NgramField(model_attr='content')
    def get_model(self):
        return postblog
    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-timedata')
