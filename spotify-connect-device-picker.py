import os
import spotipy
import spotipy.util as util
import sys

#at time of writing, the connect APIs are new and not in Spotipy itself
class SpotifyConnect(spotipy.Spotify):
    def connect_devices(self):
        return self._get('me/player/devices')

    def select_device(self, device_id):
        return self._put('me/player', payload={'device_ids': [device_id]})

def print_devices(devices, as_menu=True):
    for iteration, device in enumerate(devices):
        print(f"[{iteration+1}] ", end='') if as_menu else None
        active_indicator = ('* ' if device['is_active'] else '  ') if as_menu else ''
        print(f"{active_indicator}{device['name']}")

def read_player_index(player_count):
    player_index = None
    devices_range = range(0, player_count)
    while player_index is None:
        try:
            player_index = int(input('Select player index: ')) - 1
            if player_index not in devices_range:
                player_index = None
                raise ValueError()
        except KeyboardInterrupt:
            #Squelch exception and exit quietly
            print()
            sys.exit(0)
        except ValueError:
            print(f'Please enter a number between 1 and {player_count}\n')
    return player_index

scope = 'user-read-playback-state user-modify-playback-state'
username = os.environ['SPOTIFY_USERNAME']
token = util.prompt_for_user_token(username, scope)

sp = SpotifyConnect(auth=token)
devices = sp.connect_devices()['devices']
devices = sorted(devices, key=lambda k: k['name'])

device = None
if len(sys.argv) >= 2:
    device_name = sys.argv[1]
    if device_name == '-l': #I hope that isn't a valid device name...
        #Special case, list out device name line by line
        print_devices(devices, as_menu=False)
        sys.exit(0)

    device = next((device for device in devices if device['name'] == device_name), None)
    if device is None:
        print(f"ERROR: Device '{device_name}' not selectable")
        sys.exit(1)
else:
    print_devices(devices)
    device = devices[read_player_index(len(devices))]

print(f"Selected '{device['name']}'")

sp.select_device(device['id'])
