from yt_dlp import YoutubeDL
import os

def baixar_mp3(url):
    try:
        # Configurações para download de áudio MP3
        ydl_opts = {
            'format': 'bestaudio/best',  # Melhor qualidade de áudio
            'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',  # Extrai o áudio
                    'preferredcodec': 'mp3',  # Formato MP3
                    'preferredquality': '192',  # Qualidade do áudio (192 kbps)
                }
            ],
        }

        print("Baixando áudio...")
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            titulo = info.get('title', 'audio')
            
        print("Download e conversão para MP3 concluídos!")
        return titulo

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

# Versão com pasta específica para downloads
def baixar_mp3_com_pasta(url, pasta="downloads_mp3"):
    try:
        # Criar pasta se não existir
        if not os.path.exists(pasta):
            os.makedirs(pasta)
        
        # Configurações para download de áudio MP3
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(pasta, '%(title)s.%(ext)s'),  # Salva na pasta
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],
            'quiet': False,  # Mostra progresso
            'no_warnings': False,  # Mostra avisos
        }

        print("Baixando áudio...")
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            titulo = info.get('title', 'audio')
            
        print(f"Download concluído: {titulo}.mp3")
        print(f"Arquivo salvo em: {pasta}")
        return titulo

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

# Versão completa com menu interativo
def main():
    print("🎵 YouTube MP3 Downloader")
    print("=" * 30)
    
    while True:
        print("\nOpções:")
        print("1 - Baixar MP3")
        print("2 - Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '2':
            print("Saindo...")
            break
            
        elif opcao == '1':
            url = input("Insira a URL do vídeo: ").strip()
            if url:
                # Perguntar se quer pasta personalizada
                usar_pasta = input("Usar pasta personalizada? (s/n): ").strip().lower()
                
                if usar_pasta == 's':
                    nome_pasta = input("Nome da pasta: ").strip() or "downloads_mp3"
                    baixar_mp3_com_pasta(url, nome_pasta)
                else:
                    baixar_mp3_com_pasta(url)
            else:
                print("URL inválida!")
                
        else:
            print("Opção inválida!")

# Exemplo de uso simples
if __name__ == "__main__":
    # Para uso direto (descomente uma das linhas abaixo):
    
    # 1. Uso simples:
    # url_audio = input("Insira a URL do vídeo: ")
    # baixar_mp3(url_audio)
    
    # 2. Com pasta específica:
    # url_audio = input("Insira a URL do vídeo: ")
    # baixar_mp3_com_pasta(url_audio, "minhas_musicas")
    
    # 3. Menu interativo:
    main()
