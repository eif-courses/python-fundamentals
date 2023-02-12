class Course:

    def __init__(self, link, description, image):
        self.link = link
        self.description = description
        self.image = image
    def __repr__(self):
        return f'Hi, ..{self.link}..{self.description}..{self.image}'
