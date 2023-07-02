import yt_dlp
import os

def get_user_input(prompt):
    return input(prompt + ": ")

def download_playlist(playlist_url, output_folder, start_index, end_index):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(playlist_index)s-%(title)s.%(ext)s'),
        'playliststart': start_index,
        'playlistend': end_index,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def main():
    playlist_url = get_user_input("Enter the playlist URL")
    output_folder = get_user_input("Enter the output folder")
    start_index = get_user_input("Enter the start index (optional, default is 1)")
    end_index = get_user_input("Enter the end index (optional, default is last)")

    if not start_index:
        start_index = 1
    if not end_index:
        end_index = None

    download_playlist(playlist_url, output_folder, start_index, end_index)

if __name__ == "__main__":
    main()
