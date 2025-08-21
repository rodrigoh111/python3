Configuracao:

Instalar python3-pip python3-venv ffmpeg
apt install ffmpeg python3-pip python3-venv -y

Criar ambiente:

python3 -m venv venv
source venv/bin/activate
pip install yt-dlp
python3 baixar_yt_mp3.py

Insira a URL do youtube para baixar.

Sair do ambiente virtual do python


Obs:

Opções de qualidade de áudio:
Você pode alterar a qualidade modificando 'preferredquality':
'128' - Qualidade padrão
'192' - Qualidade boa (recomendado)
'256' - Qualidade alta
'320' - Qualidade máxima

