def create_youtube_video(title,description,list1):
	new_video={"title":title , "description":description , "likes":0 , "dislikes":0 , "comments": {},"hashtag":list1}
	return new_video
	
def likes(new_video):

	if "likes" in new_video:
		new_video ["likes"] +=1
		return new_video

def dislikes(new_video):

	if "dislikes" in new_video:
		new_video ["dislikes"] +=1
	return new_video

def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

newyoutubevideo = create_youtube_video("Eating video","Animals in the Rainforest")
for i in range(496):
	newyoutubevideo = likes(newyoutubevideo)
newyoutubevideo = dislikes(newyoutubevideo)
newyoutubevideo = add_comment(newyoutubevideo , "username" , "comment")
print(newyoutubevideo)

def hashtag1():
	list1=[]
    i=0
    a=0
    print("Put . if you are done!")
    while a!='.' and i<=5:
    	a=input()
    	list1.append(a)
    	i+=1
    if "." in list1:
    	list1.remove(".")
    return list1






