from sqlmodel import SQLModel, Field, Column, DateTime, Relationship
from sqlalchemy.sql import func
from datetime import datetime
from typing import List


class SongBase(SQLModel):
    name: str


class Song(SongBase, table=True):
    __tablename__ = 'songs'
    id: int = Field(default=None, primary_key=True)
    album_id: int = Field(foreign_key='albums.id', nullable=False)
    # date_creation: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False, index=True, server_default=func.now()))
    # date_update: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False, index=True, server_default=func.now(), onupdate=func.now()))
    album: "Album" = Relationship(back_populates='songs')


class SongCreate(SongBase):
    album: str


class AlbumBase(SQLModel):
    name: str


class Album(AlbumBase, table=True):
    __tablename__ = 'albums'
    id: int = Field(default=None, primary_key=True)
    artist_id: int = Field(foreign_key='artists.id', nullable=False)
    artist: "Artist" = Relationship(back_populates='albums')
    songs: "Song" = Relationship(back_populates='album')


class AlbumCreate(AlbumBase):
    artist: str


class ArtistBase(SQLModel):
    name: str = Field(unique=True)


class Artist(ArtistBase, table=True):
    __tablename__ = 'artists'
    id: int = Field(default=None, primary_key=True)
    albums: List[Album] = Relationship(back_populates='artist')


class ArtistCreate(ArtistBase):
    pass
