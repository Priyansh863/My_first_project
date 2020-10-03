__author__ = 'PRIYANSH KHANDELWAL'
'''
from rest_framework.routers import DefaultRouter
from industrial_project_app import views
router=DefaultRouter()
router.register(r'state',views.Stat_views,basename='state')
router.register(r'city',views.City_View,basename='city')
router.register(r'Client_views',views.client_view,basename='client_view')
router.register(r'Institute_views',views.Institute_views,basename='Institute')
router.register(r'Post_views',views.Post_views,basename='Post_views')
router.register(r'Post_get',views.Post_get,basename='Post_get')
router.register(r'Like_views',views.Like_views,basename='Like_views')
router.register(r'UnLike_views',views.UnLike_views,basename='UnLike_views')
router.register(r'Comment_views',views.Comment_views,basename='Comment_views')
router.register(r'Friend_request',views.Friend_request,basename='Friend_request')
router.register(r'client_update',views.client_update,basename='client_update')

router.register(r'login_client',views.login_client1,basename='login_client')
router.register(r'technical',views.technical_view,basename='technical')
router.register(r'nontechnical',views.nontechnical_view,basename='nontechnical')
router.register(r'institute_get',views.institute_get,basename='institute_get')
router.register(r'post_content_view',views.post_content_view,basename='post_content_view')




















urlpatterns=router.urls

'''''