# Django_projects
Hi all, there my projects on Django as beginer, from single projects to complex one

the project 'fifth' use django rest framework and database with using sqlite3, it's train project, there my api and information about them.

path('api/v1/autorization/',include('rest_framework.urls')), - working like django admin autarization

path('api/v1/Account/',AccountCreate.as_view()), - Post,Get request
    
path('api/v1/Account/<int:pk>/',AccountUpdate.as_view()),Put,Delete Request
    
path('api/v1/Account/del/<int:pk>/',AccountDelete.as_view()),Delete Request
    
path('api/v1/Account+/<int:pk>/',AccountALL.as_view()),Put,Get,Delete Request
    
path('api/v1/auth/', include('djoser.urls')), - functions for users database like examole api/v1/auth/users
    
re_path(r'^auth/', include('djoser.urls.authtoken')) - that give tokens for autarization
