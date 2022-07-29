from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE))

    def add_photo(self, label):
        for row in range(len(self.photos)):
            if len(self.photos[row]) < self.PHOTOS_PER_PAGE:
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"
        return "No more free slots"

    def display(self):
        separator = '-' * 11 + '\n'
        result = separator
        for page in range(len(self.photos)):
            pictures = '[] ' * len([p for p in self.photos[page]]) + '\n'
            result += pictures
            result += separator
        return result.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))

print(album.add_photo("first grade"))

print(album.add_photo("eight grade"))

print(album.add_photo("party with friends"))

print(album.photos)

print(album.add_photo("prom"))

print(album.add_photo("wedding"))

print(album.display())