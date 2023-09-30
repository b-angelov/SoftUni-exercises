from project.decoration.base_decoration import BaseDecoration
from project.common_functions import get_from_collection_or_error

class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        return get_from_collection_or_error(self.decorations,"decoration_type",decoration_type,do_not_raise_error=True) or "None"