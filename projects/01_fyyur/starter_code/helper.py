def format_show(show):
    # formatted_show =
    return {
        "venue_id": show.venue.id,
        "venue_name": show.venue.name,
        "artist_id": show.artist.id,
        "artist_name":show.artist.name,
        "artist_image_link": show.artist.image_link,
        "start_time": str(show.start_time)
      }
