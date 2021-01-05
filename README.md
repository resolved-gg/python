# reSolved python library

reSolved is an upcoming captcha solving service, capable of solving reCaptcha, hCaptcha, GeeTest as fast as sub 5 seconds. reSolved is designed to handle heavy workloads, unlike other captcha solving services. 

We strive to improve the reSolved experience every single day - which is why we are releasing libraries that make an already simple integration process completely seamless.


# Getting Started
### Installation
```
pip install reSolved
```


### Import the library
```py
from resolved.domlabs import Resolved
```

### Initialize an object
```py
resolved = ReSolved('0fdd7a34-16ff-4ab7-a28b-566ff425c12c', '264f06d413e71211d66a4ff42b2076')

```


### Create a task and get the solved captcha token
```py
task = resolved.createTask(
        SITE_KEY",              # string
        SITE_URL,               # string
        CAPTCHA_SERVICE",       # string - e.g., reCaptcha, hCaptcha etc
        CAPTCHA_TYPE,           # string - e.g, v2Invis/v2
        SESSION_CLONE,          # boolean
        SMART_MOVEMENT,         # boolean
        PROXY)                  # string - e.g., http://ip:port:username:password

taskID = task['data']['taskID']
token = resolved.getToken()
```

# Full code example
```py
# import library
from src.reSolved import ReSolved

# create a resolved object
resolved = ReSolved('0fdd7a34-16ff-4ab7-a28b-566ff425c12c', '264f06d413e71211d66a4ff42b2076')

# create a task
task = resolved.createTask(
        SITE_KEY",              # string
        SITE_URL,               # string
        CAPTCHA_SERVICE",       # string - e.g., reCaptcha, hCaptcha etc
        CAPTCHA_TYPE,           # string - e.g, v2Invis/v2
        SESSION_CLONE,          # boolean
        SMART_MOVEMENT,         # boolean
        PROXY)                  # string - e.g., http://ip:port:username:password

taskID = task['data']['taskID']

# store the token
token = resolved.getToken()
```
