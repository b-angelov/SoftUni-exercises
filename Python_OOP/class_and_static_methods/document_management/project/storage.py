from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = [category for category in self.categories if category_id == category.id][0]
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [topic for topic in self.topics if topic_id == topic.id][0]
        topic.id = topic_id
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = [document for document in self.documents if document_id == document.id][0]
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [category for category in self.categories if category.id == category_id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [topic for topic in self.topics if topic_id == topic.id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [document for document in self.documents if document_id == document.id][0]
        self.documents.remove(document)

    def get_document(self, document_id):
        return [document for document in self.documents if document_id == document.id][0]

    def __repr__(self):
        return '\n'.join(str(document) for document in self.documents)
