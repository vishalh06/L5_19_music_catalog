"""Manage a music catalog and serialize playlists using JSON."""

import json
import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE songs ("
    "id INTEGER PRIMARY KEY, title TEXT, artist TEXT, plays INTEGER)"
)


def add_song(title, artist, plays=0, playlist=None):
    """Add a song to the catalog and return its playlist."""
    if playlist is None:
        playlist = []
    conn.execute(
        "INSERT INTO songs (title, artist, plays) VALUES (?, ?, ?)",
        (title, artist, plays),
    )
    playlist.append(title)
    return playlist


def shuffle_pick():
    """Return a random song ID, or None when the catalog is empty."""
    ids = [row[0] for row in conn.execute("SELECT id FROM songs")]
    return secrets.choice(ids) if ids else None


def popularity(title):
    """Classify a song using its play count."""
    row = conn.execute(
        "SELECT plays FROM songs WHERE title = ?", (title,)
    ).fetchone()
    if row is None:
        return "unknown"
    return "popular" if row[0] > 100 else "niche"


def save_playlist(playlist):
    """Serialize a playlist as JSON text."""
    return json.dumps(playlist)


def load_playlist(blob):
    """Deserialize a playlist from JSON text."""
    return json.loads(blob)


def total_plays():
    """Return total plays, or zero for an empty catalog or database error."""
    try:
        row = conn.execute("SELECT SUM(plays) FROM songs").fetchone()
        return row[0] if row[0] is not None else 0
    except sqlite3.Error:
        return 0


def main():
    """Run a short demonstration of the catalog."""
    playlist = add_song("Aurora", "Nila", 250)
    add_song("Monsoon", "Kavya", 40, playlist)
    blob = save_playlist(playlist)
    loaded_playlist = load_playlist(blob)
    if len(loaded_playlist) > 1:
        print("multi-song playlist")
    print(
        popularity("Aurora"),
        popularity("Monsoon"),
        shuffle_pick(),
        total_plays(),
    )


if __name__ == "__main__":
    try:
        main()
    finally:
        conn.close()
