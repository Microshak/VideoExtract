

from pytube import YouTube
from moviepy.editor import *

PodCasts = []
PodCasts.append('https://www.youtube.com/watch?v=EfB2kprG7es')
PodCasts.append('https://www.youtube.com/watch?v=srB97uc_HVA&list=PLKDy1iUuItpza93BF2pt3LRN15Re6D4mc&index=15')
PodCasts.append('https://www.youtube.com/watch?v=TYDphDjFqZs')
PodCasts.append('https://www.youtube.com/watch?v=c2DeAhqbKlY')
PodCasts.append('https://www.youtube.com/watch?v=Gh0rFKjDdYg&list=PLKDy1iUuItpza93BF2pt3LRN15Re6D4mc&index=1')
PodCasts.append('https://www.youtube.com/watch?v=KLDoQoxQI_0&list=PLKDy1iUuItpza93BF2pt3LRN15Re6D4mc&index=2')
PodCasts.append('https://www.youtube.com/watch?v=2O4U1f2kRtQ&list=PLKDy1iUuItpza93BF2pt3LRN15Re6D4mc&index=4')

PodCasts.append('https://www.youtube.com/watch?v=fUV7yzWy2cQ&list=PLKDy1iUuItpza93BF2pt3LRN15Re6D4mc&index=6')

PodCasts.append('https://www.youtube.com/watch?v=Mc0J6-VOHGg&list=PLKDy1iUuItpza93BF2pt3LRN15Re6D4mc&index=7')



for casts in PodCasts:
  #YouTube(casts).streams.first().download()
  


  yt = YouTube(casts)
  file = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
  video = VideoFileClip(file)
  audiofile = file.replace('mp4', "mp3")
  video.audio.write_audiofile(audiofile)
