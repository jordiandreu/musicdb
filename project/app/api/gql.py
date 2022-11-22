from typing import List
from fastapi import Depends
from sqlalchemy.future import select
from sqlalchemy import join
from sqlalchemy.ext.asyncio import AsyncSession
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info

from app.db import get_session
from app.models import Song, Album, Artist
from app.schema import SongQuery, AlbumQuery, ArtistQuery
from app.schema import ArtistType


async def get_context(
    session=Depends(get_session)
):
    return {'session': session}

# TODO: use JOIN in queries
@strawberry.type
class Query:
    
    @strawberry.field
    async def songs(self, info: Info) -> List[SongQuery]:
        session = info.context['session']
        result = await session.execute(select(Song))
        songs = result.scalars().all()
        song_list = []
        for song in songs:
            album = await get_album_from_song(song, session)
            artist = await get_artist_from_album(album, session)
            song_list.append(SongQuery(name=song.name, album=album.name, artist=artist.name))
        return song_list

    @strawberry.field
    async def albums(self, info: Info) -> List[AlbumQuery]:
        session = info.context['session']
        result = await session.execute(select(Album))
        albums = result.scalars().all()
        album_list = []
        for album in albums:
            artist = await get_artist_from_album(album, session)
            songs = await get_songs_from_album(album, session)
            album_list.append(AlbumQuery(name=album.name, artist=artist.name, songs=songs))
        return album_list

    @strawberry.field
    async def artists(self, info: Info) -> List[ArtistQuery]:
        session = info.context['session']
        result = await session.execute(select(Artist))
        artists = result.scalars().all()
        artist_list = []
        for artist in artists:
            albums = await get_albums_from_artist(artist, session)
            album_list = []
            for album in albums:
                songs = await get_songs_from_album(album, session)
                album_list.append(AlbumQuery(name=album.name, artist=artist.name, songs=songs))
            artist_list.append(ArtistQuery(name=artist.name, albums=album_list))
        return artist_list


async def get_album_from_song(song: Song, session: AsyncSession) -> Album:
    result = await session.execute(select(Album).where(Album.id == song.album_id))
    album = result.scalars().first()
    return album


async def get_artist_from_album(album: Album, session: AsyncSession) -> Artist:
    result = await session.execute(select(Artist).where(Artist.id == album.artist_id))
    artist = result.scalars().first()
    return artist


async def get_albums_from_artist(artist: Artist, session: AsyncSession) -> List[Album]:
    result = await session.execute(select(Album).where(Album.artist_id == artist.id))
    albums = result.scalars().all()
    return albums


async def get_songs_from_album(album: Album, session: AsyncSession) -> List[Song]:
    result = await session.execute(select(Song).where(Song.album_id == album.id))
    songs = result.scalars().all()
    return songs


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_artist(self, name: str, info: Info) -> ArtistType:
        session = info.context['session']
        artist = Artist(name=name)
        session.add(artist)
        await session.commit()
        await session.refresh(artist)
        return artist

schema = strawberry.Schema(query=Query, mutation=Mutation)
router = GraphQLRouter(schema, context_getter=get_context)
