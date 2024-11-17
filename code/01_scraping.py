import os
from dotenv import load_dotenv
import pandas as pd
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
from bs4 import BeautifulSoup
import unidecode
import re


# Función para inicializar el cliente de Spotify
def initialize_spotify_client(client_id: str, client_secret: str) -> spotipy.Spotify:
    auth_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
    return spotipy.Spotify(auth_manager=auth_manager)


# Función para obtener todos los álbumes de un artista
def get_albums(sp: spotipy.Spotify, artist_name: str) -> list[dict[str, any]]:
    results = sp.search(q=artist_name, type="artist", limit=1)
    artist_id = results["artists"]["items"][0]["id"]

    albums = []
    results = sp.artist_albums(artist_id, limit=50, album_type="album")
    albums.extend(results["items"])

    while results["next"]:
        results = sp.next(results)
        albums.extend(results["items"])

    return albums


# Función para obtener las canciones de un álbum
def get_tracks_from_album(sp: spotipy.Spotify, album_id: str) -> list[dict[str, any]]:
    tracks = []
    results = sp.album_tracks(album_id)
    tracks.extend(results["items"])

    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])

    return tracks


# Función para obtener las características de audio de las canciones
def get_audio_features(
    sp: spotipy.Spotify, track_ids: list[str]
) -> list[dict[str, any]]:
    return sp.audio_features(track_ids)


# Función principal para extraer información de un artista
def fetch_artist_data(
    sp: spotipy.Spotify, artist_name: str, pause_time: float = 1.0
) -> pd.DataFrame:
    albums = get_albums(sp, artist_name)

    song_data = []

    for album in albums:
        album_name = album["name"]
        album_id = album["id"]
        album_release_date = album["release_date"]
        album_type = album["album_type"]

        tracks = get_tracks_from_album(sp, album_id)

        for track in tracks:
            track_id = track["id"]
            track_name = track["name"]
            track_duration_ms = track["duration_ms"]

            audio_features = get_audio_features(sp, [track_id])[0]

            song_data.append(
                {
                    "album_name": album_name,
                    "album_id": album_id,
                    "album_release_date": album_release_date,
                    "album_type": album_type,
                    "track_name": track_name,
                    "track_id": track_id,
                    "track_duration_ms": track_duration_ms,
                    "track_tempo": audio_features["tempo"],
                    "track_key": audio_features["key"],
                    "track_mode": audio_features["mode"],
                    "track_danceability": audio_features["danceability"],
                    "track_energy": audio_features["energy"],
                    "track_loudness": audio_features["loudness"],
                    "track_speechiness": audio_features["speechiness"],
                    "track_acousticness": audio_features["acousticness"],
                    "track_instrumentalness": audio_features["instrumentalness"],
                    "track_liveness": audio_features["liveness"],
                    "track_valence": audio_features["valence"],
                    "track_time_signature": audio_features["time_signature"],
                }
            )

        # Pausar para evitar el límite de la API
        time.sleep(pause_time)

    df = pd.DataFrame(song_data)
    return df


# Función para obtener la letra de la canción de Lyrics On Demand
def get_lyrics_from_lyricsondemand(
    artist: str, song_title: str, base_url: str = "https://lyricsondemand.com"
) -> str | None:
    # Normalizar nombres eliminando acentos y espacios
    artist = unidecode.unidecode(artist.lower()).replace(" ", "") + "lyrics"
    song_title = unidecode.unidecode(song_title.lower()).replace(" ", "") + "lyrics"

    # Construir la URL de la canción
    url = f"{base_url}/s/{artist}/{song_title}.html"

    # Hacer la solicitud GET al sitio web
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Buscar el div que contiene la letra
        lyrics_div = soup.find("div", class_="lcontent")
        if lyrics_div:
            # Convertir líneas separadas por <br> en texto plano
            lyrics = lyrics_div.get_text(separator=" ", strip=True)
            return lyrics

    return None


# Función para procesar un archivo TSV y obtener letras de canciones
def process_lyrics(
    input_file: str,
    artist_name: str,
) -> pd.DataFrame:
    # Leer el archivo TSV
    spotify_df = pd.read_csv(input_file, sep="\t")

    # Lista para almacenar las letras
    lyrics_data: list[dict[str, str]] = []

    # Iterar sobre las filas del DataFrame
    for _, row in spotify_df.iterrows():
        track_name = row["track_name"]
        # Limpiar el nombre de la canción (remover subtítulos entre paréntesis o guiones)
        song_name = re.split(r"[-\(]", track_name)[0].strip()

        # Obtener la letra
        lyrics = get_lyrics_from_lyricsondemand(artist_name, song_name)
        if lyrics:
            lyrics_data.append(
                {"artist_name": artist_name, "song_name": song_name, "lyrics": lyrics}
            )

    # Convertir la lista de resultados a un DataFrame
    lyrics_df = pd.DataFrame(lyrics_data)

    return lyrics_df


def main():
    # Cargar las variables de entorno desde el archivo .env
    load_dotenv()

    # Asigno los valores a las constantes
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

    ARTIST_NAME = "Soda Stereo"

    SONGS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "songs.tsv")
    LYRICS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "lyrics.tsv")

    # Verificar si el archivo songs ya existe
    if not os.path.exists(SONGS_FILE):
        spotify_client = initialize_spotify_client(
            SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
        )
        songs_df = fetch_artist_data(spotify_client, ARTIST_NAME)
        songs_df.to_csv(SONGS_FILE, sep="\t", index=False)

    # Verificar si el archivo lyrics ya existe
    if not os.path.exists(LYRICS_FILE):
        lyrics_df = process_lyrics(SONGS_FILE, LYRICS_FILE, ARTIST_NAME)
        lyrics_df.to_csv(LYRICS_FILE, sep="\t", index=False)


if __name__ == "__main__":
    main()
