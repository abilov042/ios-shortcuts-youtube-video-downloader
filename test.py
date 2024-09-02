import yt_dlp

def download(link):
    ydl_opts = {
        'format': 'best',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download is completed successfully")
    except Exception as e:
        print(f"An error has occurred: {e}")

link = input("Enter the YouTube video URL: ")
download(link)
