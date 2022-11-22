
# New Artist:

curl -X POST -H "Content-Type: application/json" -d '{"name": "Metallica"}' http://localhost:8004/artists

curl -X POST -H "Content-Type: application/json" -d '{"name": "And justice for all", "artist": "Metallica"}' http://localhost:8004/albums

curl -X POST -H "Content-Type: application/json" -d '{"name": "Blackened", "album": "And justice for all"}' http://localhost:8004/songs
curl -X POST -H "Content-Type: application/json" -d '{"name": "...and justice for all", "album": "And justice for all"}' http://localhost:8004/songs
curl -X POST -H "Content-Type: application/json" -d '{"name": "Eye of the beholder", "album": "And justice for all"}' http://localhost:8004/songs
curl -X POST -H "Content-Type: application/json" -d '{"name": "One", "album": "And justice for all"}' http://localhost:8004/songs

curl -X POST -H "Content-Type: application/json" -d '{"name": "Black album", "artist": "Metallica"}' http://localhost:8004/albums

curl -X POST -H "Content-Type: application/json" -d '{"name": "Enter sandman", "album": "Black album"}' http://localhost:8004/songs
curl -X POST -H "Content-Type: application/json" -d '{"name": "Sad bu true", "album": "Black album"}' http://localhost:8004/songs
curl -X POST -H "Content-Type: application/json" -d '{"name": "Holier than thou", "album": "Black album"}' http://localhost:8004/songs
curl -X POST -H "Content-Type: application/json" -d '{"name": "The unforgiven", "album": "Black album"}' http://localhost:8004/songs


curl -X POST -H "Content-Type: application/json" -d '{"name": "Porcupine Tree"}' http://localhost:8004/artists

curl -X POST -H "Content-Type: application/json" -d '{"name": "Closure/Continuation", "artist": "Porcupine Tree"}' http://localhost:8004/albums

curl -X POST -H "Content-Type: application/json" -d '{"name": "Harridan", "album": "Closure/Continuation"}' http://localhost:8004/songs
curl -X POST -H "Content-Type: application/json" -d '{"name": "Of the new day", "album": "Closure/Continuation"}' http://localhost:8004/songs
curl -X POST -H "Content-Type: application/json" -d '{"name": "Rats return", "album": "Closure/Continuation"}' http://localhost:8004/songs