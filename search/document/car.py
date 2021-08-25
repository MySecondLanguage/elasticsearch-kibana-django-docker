from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from car.models import Car

CAR_INDEX = Index('car')
CAR_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@CAR_INDEX.doc_type
class CarDocument(Document):

    id = fields.IntegerField(attr='id')

    name = fields.TextField(
        analyzer=html_strip,
        fields={'raw': fields.KeywordField()}
    )

    description = fields.TextField(
        analyzer=html_strip,
        fields={'raw': fields.KeywordField()}
    )

    type = fields.IntegerField()

   
    class Django:
        """Meta options."""

        model = Car