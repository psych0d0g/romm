from functools import cached_property

from models.base import BaseModel
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship


class BaseAsset(BaseModel):
    __abstract__ = True

    id = Column(Integer(), primary_key=True, autoincrement=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    file_name = Column(String(length=450), nullable=False)
    file_name_no_tags = Column(String(length=450), nullable=False)
    file_extension = Column(String(length=10), nullable=False)
    file_path = Column(String(length=1000), nullable=False)
    file_size_bytes = Column(Integer(), default=0, nullable=False)

    rom_id = Column(
        Integer(), ForeignKey("roms.id", ondelete="CASCADE"), nullable=False
    )

    @cached_property
    def full_path(self) -> str:
        return f"{self.file_path}/{self.file_name}"

    @cached_property
    def download_path(self) -> str:
        return f"/api/raw/{self.full_path}"


class Save(BaseAsset):
    __tablename__ = "saves"
    __table_args__ = {"extend_existing": True}

    emulator = Column(String(length=50), nullable=True)

    rom = relationship("Rom", lazy="selectin", back_populates="saves")


class State(BaseAsset):
    __tablename__ = "states"
    __table_args__ = {"extend_existing": True}

    emulator = Column(String(length=50), nullable=True)

    rom = relationship("Rom", lazy="selectin", back_populates="states")


class Screenshot(BaseAsset):
    __tablename__ = "screenshots"
    __table_args__ = {"extend_existing": True}

    rom = relationship("Rom", lazy="selectin", back_populates="screenshots")