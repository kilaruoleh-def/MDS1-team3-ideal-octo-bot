import datetime


class Note:
    def __init__(self, name):
        self.tags = set()
        self.text = ""
        self.name = name
        now = datetime.datetime.now()
        self.creating_date = now.strftime("%D-%M-%Y %H:%M:%S")

    def change_text(self, new_text):
        self.text = new_text

    def add_tag(self, new_tag):
        self.tags.add(new_tag)

    def remove_tag(self, new_tag):
        if new_tag not in self.tags:
            raise KeyError
        self.tags.remove(new_tag)

    def has_tag(self, search_tag):
        return search_tag in self.tags

    def show(self):
        tags = ','.join(self.tags)
        tags = 'No tags' if tags == '' else f"Tags: {tags}"
        text = 'No text' if self.text == '' else f"Text:\n{self.text}"
        return f"Title: {self.name}\n{tags}\nCreated at: {self.creating_date}\n{text}"

    def to_dict(self):
        dict__ = self.__dict__
        dict__['tags'] = list(self.tags)
        return dict__

    @classmethod
    def from_dict(cls, data):
        note = cls(data["name"])
        note.tags = set(data["tags"])
        note.text = data["text"]
        note.creating_date = data["creating_date"]
        return note
