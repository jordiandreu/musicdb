from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import init_db, get_session
from app.models import Album, AlbumCreate, Artist, ArtistCreate, Song, SongCreate


router = APIRouter()


@router.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, album_id=song.album_id, id=song.id) for song in songs]


@router.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Album).where(Album.name==song.album))
    album = result.scalars().first()
    if album:
        song = Song(name=song.name, album=album)
        session.add(song)
        await session.commit()
        await session.refresh(song)
        return song
    return


@router.get("/albums", response_model=list[Album])
async def get_albums(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Album))
    albums = result.scalars().all()
    return [Album(name=album.name, id=album.id, artist_id=album.artist_id) for album in albums]


@router.post("/albums")
async def add_album(album: AlbumCreate, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Artist).where(Artist.name==album.artist))
    artist = result.scalars().first()
    if artist:
        album = Album(name=album.name, artist=artist)
        session.add(album)
        await session.commit()
        await session.refresh(album)
        return album
    return


@router.get("/artists", response_model=list[Artist])
async def get_artists(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Artist))
    artists = result.scalars().all()
    print('******')
    print(artists)
    return [Artist(name=artist.name, id=artist.id) for artist in artists]


@router.post("/artists")
async def add_artist(artist: ArtistCreate, session: AsyncSession = Depends(get_session)):
    artist = Artist(name=artist.name)
    session.add(artist)
    await session.commit()
    await session.refresh(artist)
    return artist
