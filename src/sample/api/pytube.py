from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=AFaUCxGDZr4")
for itag_list in video.streams.all():
    print(itag_list)
stream = video.streams.get_by_itag(160)
stream.download()