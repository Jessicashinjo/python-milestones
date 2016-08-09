# Making HTTP Requests

There's an amazing Python package named [requests](http://docs.python-requests.org/en/master/user/quickstart/) that will allow you to make HTTP calls to external resources and use the response.

Here's an example of hitting your Music History data in your Firebase application, and then building a template from it. It also introduces the `json` package will will deserialize a JSON string into a Python dictionary.

##### views.py

---

```py
import requests
import json

def songs(request):
  # Make HTTP request to Firebase and get songs JSON
  song_response = requests.get('https://musichistory.firebaseio.com/songs.json')

  # Deserialize the JSON string into a dictionary
  songs = json.loads(song_response.text)

  # Set the context for the template
  context = {'songs': songs}

  # Render the template and respond to request
  return render(request, 'polls/songs.html', context)

```

##### templates/songs.html

---

```html
<h1>Songs</h1>

{% for song in songs.values %}
    <div>
      {{ song.name }}
    </div>
{% endfor %}
```