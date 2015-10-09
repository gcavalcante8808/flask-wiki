from sqlalchemy.types import TypeDecorator, CHAR
import uuid


class GUIDField(TypeDecorator):
    # Platform independent GUID Implementation that uses little endianess.
    impl = CHAR

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        else:
            if isinstance(value, uuid.UUID):
                return value.bytes_le

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(bytes_le=value)
