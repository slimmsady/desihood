from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=100)
    youtube_url = models.URLField(blank=True)
    spotify_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name}: {self.youtube_url} ||| {self.spotify_url}"


class Artist(models.Model):
    name = models.CharField("artist's stage name", max_length=60, unique=True)  # Artist's stage name, not real name
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(blank=True)
    youtube_url = models.URLField(blank=True)
    spotify_url = models.URLField(blank=True)
    # SET_NULL: set label as null if label is deleted
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.youtube_url} ||| {self.spotify_url}"


class SongArtist(models.Model):
    # Roles of an artist in the song.
    RAPPER = 'RP'
    BEAT_PRODUCER = 'BP'
    ARTIST_ROLE = [
        (RAPPER, "Rappeer"),
        (BEAT_PRODUCER, "Beat by"),
    ]
    song = models.ForeignKey("Song", on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.CharField("Rap / Beat", max_length=2, choices=ARTIST_ROLE, default=RAPPER)
    feat = models.BooleanField()


class Song(models.Model):
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist, through=SongArtist, related_name="songs")
    released_in = models.DateField(blank=True)
    youtube_url = models.URLField(blank=True)
    spotify_url = models.URLField(blank=True)
    languages = models.ManyToManyField("Language")
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artists} ({self.languages})"


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
