import datetime
from typing import Set, Dict


class Note:
    def __init__(self, name: str):
        self.tags: Set[str] = set()
        self.text: str = ""
        self.name: str = name
        self.creating_date: str = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def change_text(self, new_text: str) -> None:
        """Change the text of the note."""
        self.text = new_text

    def add_tag(self, new_tag: str) -> None:
        """Add a new tag to the note."""
        self.tags.add(new_tag)

    def remove_tag(self, new_tag: str) -> None:
        """Remove a tag from the note."""
        if new_tag not in self.tags:
            raise KeyError("Tag not found.")
        self.tags.remove(new_tag)

    def has_tag(self, search_tag: str) -> bool:
        """Check if the note has a specific tag."""
        return search_tag in self.tags

    def show(self) -> str:
        """Display the note's information."""
        tags = 'No tags' if not self.tags else f"Tags: {', '.join(self.tags)}"
        text = 'No text' if not self.text else f"Text:\n{self.text}"
        return f"Title: {self.name}\n{tags}\nCreated at: {self.creating_date}\n{text}"

    def to_dict(self) -> Dict[str, str]:
        """Convert the note to a dictionary."""
        return {
            "name": self.name,
            "tags": list(self.tags),
            "text": self.text,
            "creating_date": self.creating_date
        }

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'Note':
        """Create a Note instance from a dictionary."""
        note = cls(data["name"])
        note.tags = set(data["tags"])
        note.text = data["text"]
        note.creating_date = data["creating_date"]
        return note
