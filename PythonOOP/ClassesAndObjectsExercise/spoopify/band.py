from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = list()

    def add_album(self, album: Album):
        for collection in self.albums:
            if collection == album:
                return f"Band {self.name} already has {album} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album}."

    def remove_album(self, album_name: str):
        for album in self.albums:
            if str(album) == album_name:
                if album.published:
                    return f"Album has been published. It cannot be removed."
                self.albums.remove(album_name)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f'Band {self.name}' + '\n'
        for album in self.albums:
            result += f'{album.details()}' + '\n'
        return result.strip()

