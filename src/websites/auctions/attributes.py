from collections import namedtuple

attributes_names = [
            "title",
            "price",
            "description",
            "categories",
        ]
Attributes = namedtuple("Attributes", attributes_names)