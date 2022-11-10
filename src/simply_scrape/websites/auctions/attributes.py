from collections import namedtuple

offer_attributes_names = [
            "title",
            "price",
            "description",
            "categories",
        ]
OfferAttributes = namedtuple("Attributes", offer_attributes_names)