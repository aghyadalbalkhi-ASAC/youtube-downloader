from pytube import YouTube
link=input("enter your video link here ,please: ")
py=YouTube(link)

video=py.streams.all()

i=1
for numList in video:
    print(str(i)+" "+str(numList))
    i=i+1

choice_number=int(input("enter number please"))
video=video[choice_number-1]
video.download("\Downloade_Folder")
print(video)
print("downloaded sucessfuly!")