import yt_dlp
import os

#Change the playlist link you want to download
playlist_url = "https://www.youtube.com/playlist?list=PL7pkSK1xbGD6g2_BSXgScugMC1CJkkdBW"

#Any Change the location to save 
#then run this python file
#example >> python3 ytdlpPlaylistIndexDownloader.py 
output_folder = './repos/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#You can also select the range of specific files you want to download.
start_index = 3
end_index = 5

ydl_opts = {
    'outtmpl': os.path.join(output_folder, '%(playlist_index)s-%(title)s.%(ext)s'),
    'playliststart': start_index,
    'playlistend': end_index
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
