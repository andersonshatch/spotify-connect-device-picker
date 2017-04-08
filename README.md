# Spotify Connect Device Picker Script

Presents a list of available Spotify Connect devices to direct output to.

```
$ python spotify-connect-device-picker.py
[1]   Kitchen Echo
[2]   Living Room
[3]   Living Room Echo
[4] * picon
Select player index: 3
Selected 'Living Room Echo'
```

You can provide a device name as the first argument and it'll be used to set the device (if it's a valid device name), e.g.:

```
$ python spotify-connect-device-picker.py Living\ Room
Selected 'Living Room'
```

If you need to just list the available players, use `-l` as the first argument:

```
$ python spotify-connect-device-picker.py -l
Kitchen Echo
Living Room
Living Room Echo
picon
```

## Requirements

* Python 3.6 
* Depends on `spotipy` (`pip install spotipy`)
* Spotify API app ID and secret - create one at https://developer.spotify.com/my-applications
* Spotify Premium account
* Some Spotify Connect devices to send your music to

## Configuration
Requires values for the following environment variables:

* `SPOTIFY_USERNAME` - username of the Spotify account (must be a Premium account)
* `SPOTIPY_CLIENT_ID` - Client ID of your Spotify API application
* `SPOTIPY_CLIENT_SECRET` - Client Secret of your Spotify API application
* `SPOTIPY_REDIRECT_URI` - URL to redirect to after authorization (doesn't need to be real,
        but should ideally be a site under your control so you don't leak credentials)

On the first run, the app will open a page to authorize itself against your Spotify account, allow
it access and you'll be redirected to the URL specified in the `SPOTIPY_REDIRECT_URI`
environment variable. Paste the URL you were redirected to from the browser into the terminal, and it'll
save tokens to a hidden file in the current folder named `.cache-<username>`.

To logout, trash the `.cache-<username>` file.
