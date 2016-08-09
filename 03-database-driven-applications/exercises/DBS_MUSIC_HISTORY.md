# Server Generated Music History

## Setup

```
mkdir -p ~/workspace/python/exercises/music-history && cd $_
django-admin startproject musichistory
```

## Requirements

Make a Django application that will generate the basic version of the Music History application that you built in the front-end part of the cohort. Use the [`requests`](../resources/DBS_REQUESTS_PACKAGE.md) package to call your existing Firebase application that is storing your songs, and then populate a template with the JSON response.

### Song List

This will list all song names. The name of the song will be a hyperlink to show the song details.

### Song Detail

The detail view will show the following information.

1. Song name
2. Album name
3. Artist name
4. A hyperlink back to the list view

## Bonus Goal

1. Create a view at the url `/songs/new` that will respond with a form with a field for song name, album name and artist name.
1. The form will POST to the `/songs/create` url, and then use the `requests.post()` method to create a new song in the Firebase collection.
1. Once the song is created, redirect the user to the song list view.


