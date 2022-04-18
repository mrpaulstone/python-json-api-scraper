import requests
import json
import time
from pathlib import Path

# Creates a dumps subfolder if it does not yet exist
Path("dumps").mkdir(parents=True, exist_ok=True)

# Function for saving an API Json url to a file
def url_to_json(url,filename):
    r = requests.get(url)
    data = r.text
    parsed = json.loads(data)
    timestr = time.strftime("_%d_%m_%Y_%H_%M_%p")
    dumps = "dumps/"
    ext = ".json"
    final_filename = dumps + filename + timestr + ext

    with open(final_filename, "w") as data_file:
        json.dump(parsed, data_file, indent=4, sort_keys=True)

    return final_filename


longertest = "https://jsonplaceholder.typicode.com/todos/"
shorttest = "https://jsonplaceholder.typicode.com/todos/1"

def makeithappen():
    print("Testing small dump")
    short_test = url_to_json(shorttest, 'short_test')
    print("Small test dump complete, saved as: " + short_test)
    longertest_file = url_to_json(longertest, 'longer_test')
    print ("Longer test File saved into dumps folder as: " + longertest_file)
    print("All Done")

makeithappen()