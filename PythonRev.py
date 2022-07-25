def create_youtube_video(title,description):
	new_video={"title":title , "description":description , "likes":0 , "dislikes":0 , "comments": {}}
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
newyoutubevideo = likes(newyoutubevideo)
newyoutubevideo = dislikes(newyoutubevideo)
newyoutubevideo = add_comment(newyoutubevideo , "username" , "comment")
print(newyoutubevideo)