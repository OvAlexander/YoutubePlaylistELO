#Resources
#https://www.youtube.com/watch?v=coZbOM6E47I
#https://github.com/googleapis/google-api-python-client/blob/main/docs/start.md
#https://developers.google.com/youtube/v3/docs
#https://www.youtube.com/watch?v=jE-SpRI3K5g&t=397s
#https://www.geeksforgeeks.org/how-to-get-the-input-from-tkinter-text-box/

#To Do
#Add GUI
#ELO Rating system
#Implement audio
#web dev?
import os
import random
import tkinter as tk
from tkinter import Canvas, filedialog, Text
from googleapiclient.discovery import build

root = tk.Tk()

def loadPlaylist():
    playlistURL= playlistInput.get(0)
    print(playlistURL)

canvas = tk.Canvas(root,height=700, width=700,bg="#123456")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

playlistInput = tk.Text(frame, height =5, width=20)
playlistInput.pack()
loadPlaylist = tk.Button(root, text="Load Playlist", 
                        padx=10,pady=5,fg="white",
                        bg="#123456", command=loadPlaylist)

loadPlaylist.pack()

leftVote = tk.Button(root, text="Left", padx=10,pady=5,fg="white",bg="#123456")
rightVote = tk.Button(root, text="Right", padx=10,pady=5,fg="white",bg="#123456")

leftVote.pack()
rightVote.pack()

root.mainloop()
api_key = os.environ.get('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)

nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails', 
        playlistId='PL6-hNkdzPzFoO1i0i6vxJoavbq91QjuUQ',
        maxResults=50,
        pageToken=nextPageToken
    )
    pl_response = pl_request.execute()

    vid_ids = []

    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])
    print(','.join(vid_ids))

    vid_request = youtube.videos().list(
        part = "contentDetails,snippet",
        id =','.join(vid_ids)
    )
    vid_response = vid_request.execute()

    # numVids = 0
    # videos = {}
    for item in vid_response['items']:
        videoId = item['id']
        videoSnippet = item['snippet']
        videoTitle = videoSnippet['title']
        thumbnailLink = "https://img.youtube.com/vi/"+videoId+"/maxresdefault.jpg"
        videoLink = "https://www.youtube.com/watch?v="+videoId
        print(videoTitle.encode("utf-8"))
        print(thumbnailLink)
        print(videoLink)
        # numVids+=1
    nextPageToken = pl_request.get('nextPageToken')
    if not nextPageToken: break