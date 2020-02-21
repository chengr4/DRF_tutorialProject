from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # for all existing snippets
    # path('snippets/', views.snippet_list),
    # for individual snippet
    # path('snippets/<int:pk>/', views.snippet_detail),

    # class-based view
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)