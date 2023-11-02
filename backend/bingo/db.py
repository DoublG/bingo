from __future__ import annotations
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from typing import List, Optional
import datetime

from bingo.app import db

class Session(db.Model):
    __tablename__ = 'SESSIONS'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    abstract: Mapped[str] = mapped_column(String(1000))
    



