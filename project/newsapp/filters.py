from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter
from .models import Post, Category
from django.forms import DateInput


class PostFilter(FilterSet):
    date_create_after = DateTimeFilter(
        field_name='date_create',
        lookup_expr='date__gte',
        widget=DateInput(
            attrs={'type': 'date'}, 
        )
    )

    category = ModelMultipleChoiceFilter(
             field_name='post_category',
             queryset=Category.objects.all(),
             label='Category',
         )

    class Meta:
        model = Post
        fields = {'title': ['icontains']}
