class Drawable:
    def draw(self):
        raise NotImplementedError("You must implement draw on your subclass of Drawable")


class Image(Drawable):
    def __init__(self, image):
        self.image = image

    def __getattr__(self, name):
        if name.startswith('is_') and name.endswith('_pic'):
            search_term = name[3:-4]
            def term_searcher():
                return search_term in self.image
            return term_searcher

    def is_cat_pic(self):
        return 'cat' in self.image

    def draw(self):
        print(f"Drawing {self.image}")


class FilteredImage(Image):
    def __init__(self, image, filter):
        super().__init__(image)
        self.filter = filter

    def draw(self):
        print(f"Drawing {self.image!r} with {self.filter!r} filter")


fi = FilteredImage("cat-pic.png", "encuten")
fi.draw()
print(f"Is cat pic: {fi.is_cat_pic()}")