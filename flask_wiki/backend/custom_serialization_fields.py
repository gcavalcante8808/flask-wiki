from marshmallow import fields
import uuid


class GUIDSerializationField(fields.Field):
    def _serialize(self, value, attr, obj):
        if value is None:
            return value
        else:
            if isinstance(value, uuid.UUID):
                return str(value)
            else:
                return None
