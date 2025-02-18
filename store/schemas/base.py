from datetime import datetime
import uuid
from pydantic import UUID4, BaseModel, Field


class BaseSchemaModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    update_at: datetime = Field(default_factory=datetime.utcnow)
