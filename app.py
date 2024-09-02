from flask import Flask, request, send_file, jsonify
import yt_dlp
import os

app = Flask(__name__)

def download_video(link):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            video_title = info_dict.get('title', None)
            file_name = ydl.prepare_filename(info_dict)
            return file_name
    except Exception as e:
        print(f"An error has occurred: {e}")
        return None

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    link = data.get('link')
    if not link:
        return jsonify({"error": "No link provided"}), 400

    file_path = download_video(link)
    if file_path and os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({"error": "Failed to download video"}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
