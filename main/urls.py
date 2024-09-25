from django.urls import path

from .views import MovieAPIView, CategoryAPIView, CommentAPIView

urlpatterns = [
    path('movie/', MovieAPIView.as_view()),
    path('movie/<int:pk>/', MovieAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
    path('category/<int:pk>/', CategoryAPIView.as_view()),
    path('comment/', CommentAPIView.as_view()),
    path('comment/<int:pk>/', CommentAPIView.as_view())
]

