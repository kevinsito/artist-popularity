class Artist:
    def __init__(self, id, name, img, followers, popularity):
        self.id = id
        self.name = name
        self.img = img
        self.followers = followers
        self.popularity = popularity
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'img': self.img,
            'followers': self.followers,
            'popularity': self.popularity
        }
    
class Track:
    def __init__(self, id, name, album, popularity, release_date, img, duration_ms=None):
        self.id = id
        self.name = name
        self.album = album
        self.popularity = popularity
        self.release_date = release_date
        self.img = img
        self.duration_ms = duration_ms
    
    def to_dict(self):
        duration_seconds = self.duration_ms // 1000 if self.duration_ms else 0
        duration_formatted = f"{duration_seconds // 60}:{duration_seconds % 60:02d}"

        return {
            'id': self.id,
            'name': self.name,
            'album': self.album,
            'popularity': self.popularity,
            'releaseDate': self.release_date,
            'img': self.img,
            'duration': duration_formatted
        }

class SimpleTrack:
    def __init__(self, id, name, track_number, duration_ms=None):
        self.id = id
        self.name = name
        self.track_number = track_number
        self.duration_ms = duration_ms

    def to_dict(self):
        duration_seconds = self.duration_ms // 1000 if self.duration_ms else 0
        duration_formatted = f"{duration_seconds // 60}:{duration_seconds % 60:02d}"

        return {
            'id': self.id,
            'name': self.name,
            'trackNumber': self.track_number,
            'duration': duration_formatted
        }

class Album:
    def __init__(self, id, name, album_type, total_tracks, release_date, img, label, tracks=None):
        self.id = id
        self.name = name
        self.album_type = album_type
        self.total_tracks = total_tracks
        self.release_date = release_date
        self.img = img
        self.label = label
        self.tracks = tracks if tracks is not None else []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'albumType': self.album_type,
            'totalTracks': self.total_tracks,
            'releaseDate': self.release_date,
            'label': self.label,
            'img': self.img,
            'tracks': self.tracks
        }
