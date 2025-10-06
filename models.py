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
    def __init__(self, name, album, popularity, release_date, img):
        self.name = name
        self.album = album
        self.popularity = popularity
        self.release_date = release_date
        self.img = img
    
    def to_dict(self):
        return {
            'name': self.name,
            'album': self.album,
            'popularity': self.popularity,
            'releaseDate': self.release_date,
            'img': self.img
        }