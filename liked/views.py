from django.shortcuts import render

# Create your views here.

def like_it(request):
    user = request.user
    if request.method == 'POST':
        ObjectId = int(request.POST['objectid'])
        Tip = str(request.POST['contentType'])

        likes = LikeModel.objects.filter(object_id=ObjectId) # in here we filtered the particular post with its id
        if likes: # if the particular post is there
            if str(user) in str(likes): # then we check the user which is us, in there
                like_obj = LikeModel.objects.get(user=user,object_id=ObjectId) #if we there and we returned this data, this part for saving data, I mean if this data is already created than we dont have to delete and create again, we just change LikeModel.liked true or false state, so that if you create like and it will never delete, it just change liked or like state
            else:
                pass

        if Tip == 'UserPost':
            post_content_type_by = UserPost.objects.all().first()

            if str(user) not in str(likes):
                like = LikeModel.objects.create(user=user,liked=True,content_type=post_content_type_by.get_content_type,object_id=ObjectId)
                like.save() # if data is created then we say 'new'
                okey = 'new'

            elif str(user) in str(likes) and like_obj.liked:
                like_obj.liked = False
                like_obj.save() # if data is already there, then we save it False
                okey = 'false'

            elif str(user) in str(likes) and like_obj.liked == False:
                like_obj.liked = True
                like_obj.save() # if data is already changed to False and we save again to True
                okey = 'true'


    return render(request,'ajaxlike.html',{'likes':likes,'okey':okey})
tr