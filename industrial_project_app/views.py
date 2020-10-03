from django.shortcuts import render
'''
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from industrial_project_app.models import State,City,User_table,post,Like,UnLike,Comment,FriendRequest,User_info,Technical,NonTechnical,Institute
from  django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter

from industrial_project_app.serializers import State_serializer,City_serializer,ClientSerializer,Institute_serializer,Post_serializer,Post_serializer_get,Like_serializer,UnLike_serializer,Comment_serializer,FriendRequest_serializer,ClientSerializer_update,login_client,technical,non_technical,InstituteSerializer_get,InstituteSerializer_get,Post_serializer_get

 #Create your views here.
class Stat_views(viewsets.ViewSet):
    http_method_names =['put','patch','get']

    def create(self,request):

        serializers=State_serializer(data=request.data)
        if serializers.is_valid():

            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
    def list(self,request):
        queryset=State.objects.all()
        serializer=State_serializer(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)



class client_view(viewsets.ViewSet):
     def create(self,request):

        serializers=ClientSerializer(data=request.data)
        print('-----------------------------------------------------------------------------------------')
        if serializers.is_valid():

            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)



class client_update(viewsets.ViewSet):
    http_method_names =['put','patch','get']
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def partial_update(self, request,pk=None):
        print('joo')
        try:

            user_related=User.objects.get(username=request.user)
        except:
            return Response('login issue occur')
        print(user_related,'==============================================================================================')
        try:

            user=User_info.objects.get(id=pk)
        except:
            return Response('login issue occur')

        print(user,'pppppppppppppppppppppppppppp')


        p=request.data
        print(p,'hi')

        user.Institute=request.data.get('Institute',user.Institute)
        #print(user.name,'iiiiiiiiiiiiiiiiiiiiii')
        #user.last_name=request.data.get('last_name',user.last_name)
        #print(user.last_name,'---------------------------------------')
        try:
            t_id=request.data.get('TechnicalField',user.TechnicalField)
            user.TechnicalField=Technical.objects.get(id=t_id)

        except:
            user.TechnicalField=request.data.get('TechnicalField',user.TechnicalField)
        try:
            s_id=request.data.get('State_Name',user.State_Name)
            user.State_Name=State.objects.get(id=s_id)

        except:
            user.State_Name=request.data.get('State_Name',user.State_Name)
        try:
            c_id=request.data.get('city_Name',user.city_Name)
            user.city_Name=City.objects.get(id=s_id)

        except:
            user.city_Name=request.data.get('city_Name',user.city_Name)
        try:
            t_id=request.data.get('NonTechnicalField',user.NonTechnicalField)
            print('=====================================100000000000000000000000000000000001')
            user.NonTechnicalField=NonTechnical.objects.get(id=t_id)

        except:
            print('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[')
            user.NonTechnicalField=request.data.get(user.NonTechnicalField)
        user.Age=request.data.get('Age',user.Age)

        user.BirthDate=request.data.get('BirthDate',user.BirthDate)





        #print(user_related.driver_email,'---------------------------------------')
        user.save()
        serializer=ClientSerializer_update(user)
        print('============================================================================================')
        return Response(serializer.data)

    def list(self,request):
        queryset=User_info.objects.all()
        serializer=ClientSerializer_update(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)

    def get(self,request,pk=None):
        queryset=User_info.objects.get(id=pk)
        serializer=ClientSerializer_update(queryset)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)














class City_View(viewsets.ViewSet):

    http_method_names =['put','patch','get']

    def create(self,request):

        serializers=City_serializer(data=request.data)
        if serializers.is_valid():

            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
    def list(self,request):
        queryset=City.objects.all()
        serializer=City_serializer(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)


class Institute_views(viewsets.ViewSet):

    def create(self,request):


        serializers=Institute_serializer(data=request.data)
        print('-----------------------------------------------------------------------------------------')
        if serializers.is_valid():

            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)



class Post_views(viewsets.ViewSet):
    def create(self,request):

        serializers=Post_serializer(data=request.data)
        print('-----------------------------------------------------------------------------------------')
        if serializers.is_valid():


            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

class Post_get(viewsets.ViewSet):
    def list(self,request):

        queryset=post.objects.all()
        serializer=Post_serializer_get(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)



class Like_views(viewsets.ViewSet):
    def create(self,request):

        serializers=Like_serializer(data=request.data)
        if serializers.is_valid():

            post1=serializers.data['Post']
            print(post,'===========================================')
            c=post.objects.get(id=post1)
            c.LikeCount=c.LikeCount+1
            c.save()
            print(c,'==========c.==================================')
            user=request.user
            print(user,'oooooooooooooooooooooooooooooooooooooooooooooooooo')

            Like.objects.create(User=user,Post=c,LikeCount=1).save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)




class UnLike_views(viewsets.ViewSet):
    def create(self,request):

        serializers=UnLike_serializer(data=request.data)
        if serializers.is_valid():

            post1=serializers.data['Post']
            print(post,'===========================================')
            c=post.objects.get(id=post1)
            c.UnLikeCount=c.UnLikeCount+1
            c.save()
            print(c,'==========c.==================================')
            user=request.user
            print(user,'oooooooooooooooooooooooooooooooooooooooooooooooooo')

            UnLike.objects.create(User=user,Post=c,UnLikeCount=1).save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)



class Comment_views(viewsets.ViewSet):
    def create(self,request):
        serializers=Comment_serializer(data=request.data)
        if (serializers.is_valid()):

            user=request.user
            comment=serializers.data['Post_comment']
            post1=serializers.data['Post']
            c=post.objects.get(id=post1)
            Comment.objects.create(User=user,Post_comment=comment,Post=c).save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)






class Friend_request(viewsets.ViewSet):
    def create(self,request):
        serializers=FriendRequest_serializer(data=request.data)
        if (serializers.is_valid()):

            user=request.user
            to=serializers.data['ToUser']
            c=User.objects.get(id=to)
            FriendRequest.objects.create(FromUser=user,ToUser=c).save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)



class login_client1(viewsets.ViewSet):
    def create(self,request):
        serializers=login_client(data=request.data)
        if serializers.is_valid():

            user=serializers.data['username']
            print('ooooooooooooooooooooooo90')
            o=User.objects.get(username=user)
            login_client(request,o)
            c=User_info.objects.get(username=o)
            print('ooooooooooooooooooooooo91')
            token,created=Token.objects.get_or_create(user=o)
            return Response({"token":token.key,'success':1,"id":c.id},status=200)
        else:
            return Response(serializers.errors)



class technical_view(viewsets.ViewSet):
    def list(self,request):
        queryset=Technical.objects.all()
        serializer=technical(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)


class nontechnical_view(viewsets.ViewSet):
    def list(self,request):
        queryset=NonTechnical.objects.all()
        serializer=non_technical(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)


class institute_get(viewsets.ViewSet):
    def list(self,request):
        queryset=Institute.objects.all()
        serializer=InstituteSerializer_get(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)


class post_content_view(viewsets.ViewSet):
    def list(self,request):
        queryset=post.objects.all()
        serializer=Post_serializer_get(queryset,many=True)
        print(serializer.data,']]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        return Response(serializer.data)



'''''