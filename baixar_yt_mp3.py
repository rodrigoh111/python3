from yt_dlp import YoutubeDL

def baixar_mp3(url):
    try:
        # Configurações para download de áudio MP3
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],
        }

        print("Baixando áudio...")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download e conversão para MP3 concluídos!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso (igual ao seu código original)
url_audio = input("Insira a URL do vídeo: ")
baixar_mp3(url_audio)
