import uuid
from typing import List

from pydantic import BaseModel, ConfigDict, StringConstraints
from sqlalchemy import ARRAY, Column, String
from sqlalchemy.dialects.postgresql import UUID
from typing_extensions import Annotated, Optional

from .ext.db import db


class Pessoas(db.Model):
    __tablename__ = "pessoas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    apelido = Column(String(length=32), unique=True, nullable=False)
    nome = Column(String(length=100), nullable=False)
    nascimento = Column(String(length=10), nullable=False)
    stack = Column(ARRAY(String(length=32)))

class PessoasModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[uuid.UUID]
    apelido: Annotated[Optional[str], StringConstraints(max_length=32)]
    nome: Annotated[Optional[str], StringConstraints(max_length=100)]
    nascimento: Annotated[Optional[str], StringConstraints(max_length=10)] 
    stack: List[Annotated[str, StringConstraints(max_length=32)]]
