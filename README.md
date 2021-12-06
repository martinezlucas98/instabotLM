# InstabotLM :fire:

(By using this program you fully understand the consecuences that may happen due to the use of bots on Instagram, and fully accept what is stated at the [Disclaimer Section](#disclaimer))

InstaBotLM is a Intagram bot that aims to comment on a specific post a list of usernames (tags).

Right now, only Google Chrome browser is supported.

## Installation

### Drivers

Before anything, you must have Google Chrome installed. On this program's main folder you will see a file called **chromedriver**, this driver's version **MUST** match your Google Chrome's version.

The chromedriver that comes with this program by default is the version 89.0.4389.23.

To check your Google Chrome's version, you can type on Ubuntu's console:

```
google-chrome --version
```

Another form to check Chrome's version (that works for every OS) is by:
1. Opening Google Chrome
2. Going to `Help` (Usually by clicking the thre dots on the top right corner)
3. And finally click on `Google Chrome's Information`

To download the driver go to [this page](https://chromedriver.chromium.org/home).

Once you downloade the correct driver for your system, just replace the one that comes pre-installed.

### Requirements

The requirements.txt file contains all the requirements for this project to work.

To install this requirements you must have Python 3 and pip3 installed on your machine.

To install Python 3 and pip3 on **Ubuntu**:

```
sudo apt-get -y install python3-pip
sudo apt-get -y install python3-pip
```

For **Windows**:

Python 3.4+ in most operating systems includes pip3 by default. If your python version is less than 3.4, then you should upgrade your Python version which will automatically install pip3.

For example, you can install the latest version of Python from [ActiveState](https://www.activestate.com/products/python/), which includes pip3.

There are several other ways to do it, you will find it without any problem on the wonderful internet :earth_americas:

Once ou have Python3 and Pip3 installed, you need to install the requirements.txt using Pip3 as follows: (**Note:** you must be on the project directory)

On **Ubuntu**:

```pip3 -r requirements.txt```

Similar command for other OS.

## Execution

### First steps (Setting up)
To execute the program you **must** first edit the options.json file to match your goal. This file will look something like:

```json
{
    "username": "insert_your_username_without_@",
    "postUrl": "https://www.instagram.com/p/[INSERT POST URL]",
    "comments": 10,
    "tags": [
        "insert_username_without_@",
        "insert_username_without_@",
        "insert_username_without_@"
    ],
    "follow":"yes",
    "like":"yes"
}
```

In `username` you must specify your Instagram username without the @

In `postUrl` you must specify the URL of the post with wich you want to interact. For example: `"https://www.instagram.com/p/CWvxAY7B0ci/"`

In `comments` you must specify the number of comments you want to post on that Instagram post

In `tags` specify the usernames yo want to tag on that post (without the @). You can insert as many as you want (just remember to separate them using commas!!).

For `follow` you write `"yes` if you want to follow the account that posted the post of postURl, if you don't then write `"no"`

Similar case for the `like` field.

### Finally running the program

Now that we are all set up we can run the program.

To to this just run `python3 instabotLM.py`

This will run with the default values for "comment's interval" and "page load wait time"

The comment's interval deafult value is 120, this means that the bot will wait 120 seconds (2 minutes) between posting comments. This is to avoid triggering Instagram's anti bot mechanism (aka the bot hunter).

The page load wait time is the time our program will wait before doing anything (like inserting inputs, clicking buttons, etc) this is to ensure the page has loaded up correctly before trying to do anything. This avoids errors. It's default value is of 5 seconds.

:warning:**WARNING:**:warning: if you see any popup on instagram regarding the submission of comments, it is strongly recommended to increse the comment's interval value.

If you wish to change this values you can do it when executing the program:

`python3 instabotLM.py [COMMENT_INTERVAL] [LOAD_WAIT]`

For example if you want to have a "comment's interval" of 150 seconds and a "page load wait time" of 2 seconds, you run:

`python3 instabotLM.py 150 2`

### And what about the Password?

You will be asked to write your password on the terminal, this is all to keep it secure!! And of course, your password is not stored anywhere. 

Once you insert your password, the program will do it's magic :zap: :zap:

# DISCLAIMER

:warning: :warning:

Using bots on Instagram may get you blocked, banned, shadowbanned, or any other actions taken by Instagram to prevent and sanction the use of bots.

We are **NOT** responsible for the consecuences that may occur by using this bot.

Use it at your own risk.
