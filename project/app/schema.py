import strawberry
from typing import List
from .models import Song, Album, Artist


@strawberry.experimental.pydantic.type(model=Song)  #, all_fields=True)
class SongType:
    id: strawberry.auto
    name: strawberry.auto


@strawberry.experimental.pydantic.type(model=Song)  #, all_fields=True)
class SongQuery:
    name: strawberry.auto
    album: str
    artist: str


@strawberry.experimental.pydantic.type(model=Album)  #, all_fields=True)
class AlbumType:
    id: strawberry.auto
    name: strawberry.auto


@strawberry.experimental.pydantic.type(model=Album)  #, all_fields=True)
class AlbumQuery:
    name: strawberry.auto
    songs: List[SongQuery]
    artist: str


@strawberry.experimental.pydantic.type(model=Artist)  #, all_fields=True)
class ArtistType:
    id: strawberry.auto
    name: strawberry.auto
    albums: List[AlbumType]


@strawberry.experimental.pydantic.type(model=Artist)  #, all_fields=True)
class ArtistQuery:
    name: strawberry.auto
    albums: List[AlbumQuery]
