"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers
from quickstart import views as viewsqs
from django.contrib import admin
from snippets import views as viewsnippets
from rest_framework.urlpatterns import format_suffix_patterns

#(Tutorial 6 Refactoring to use ViewSets) 
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
# from django.urls import path, include done up
from rest_framework.routers import DefaultRouter 
# from snippets import views done up

#(Tutorial 6 Refactoring to use ViewSets) 
snippet_list = SnippetViewSet.as_view({'get': 'list','post': 'create'})
snippet_detail = SnippetViewSet.as_view({'get': 'retrieve','put': 'update','patch': 'partial_update', 'delete': 'destroy'})
snippet_highlight = SnippetViewSet.as_view({'get': 'highlight'}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve' })



router = routers.DefaultRouter()
router.register(r'users', viewsqs.UserViewSet)
router.register(r'groups', viewsqs.GroupViewSet)

#(Tutorial 6 Refactoring to use ViewSets)  Using routes
router_6 = DefaultRouter()
router_6.register(r'snippets', viewsnippets.SnippetViewSet,basename="snippet")
router_6.register(r'users', viewsnippets.UserViewSet,basename="user")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', viewsnippets.api_root),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api-auth/', include('rest_framework.urls')), #tutorial 4 Adding login to the Browsable API 
    path('snippets1/', viewsnippets.snippet_list,name='snippet_list'),
    path('snippets1/<int:pk>/', viewsnippets.snippet_detail, name='snippet_detail'),
    path('snippets_3/', viewsnippets.SnippetList.as_view(),name='viewsnippets.SnippetList'),
    path('snippets_3/<int:pk>/', viewsnippets.SnippetDetail.as_view(),name='viewsnippets.SnippetDetail'),
    path('snippets_3_Mixins/', viewsnippets.SnippetList_Mixins.as_view(),name='viewsnippets.SnippetList_Mixins'),
    path('snippets_3_Mixins/<int:pk>/', viewsnippets.SnippetDetail__Mixins.as_view(),name='viewsnippets.SnippetDetail__Mixins'), 
    path('snippets_3_Generic/', viewsnippets.SnippetList_Generic.as_view(),name='viewsnippets.SnippetList_Generic'),
    path('snippets_3_Generic/<int:pk>/', viewsnippets.SnippetDetail_Generic.as_view(),name='viewsnippets.SnippetDetail_Generic'),
    path('users/', viewsnippets.UserList.as_view(),name='viewsnippets.UserList'), #tutorial 4
    path('users/<int:pk>/', viewsnippets.UserDetail.as_view(),name='viewsnippets.UserDetail'), #Tutorial 4
    path('snippets/<int:pk>/highlight/', viewsnippets.SnippetHighlight.as_view(),name='viewsnippets.SnippetHighlight'), #no funciona
    #(Tutorial 6 Refactoring to use ViewSets) 
     path('_6/', include(router.urls)),
    path('_6_6/', api_root),
    path('snippets_6/', snippet_list, name='snippet-list'),
    path('snippets_6/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets_6/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users_6/', user_list, name='user-list'),
    path('users_6/<int:pk>/', user_detail, name='user-detail')
]
#'snippets/1/highlight/'
# urlpatterns = format_suffix_patterns(urlpatterns)

# (tutorial 5 Creating an endpoint for the highlighted snippets)
#Origina ulr file but i changed in order to expalin al modification we did.
# # API endpoints
# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),
#     path('snippets/',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     path('snippets/<int:pk>/',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     path('users/',
#         views.UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ])

