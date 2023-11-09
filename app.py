#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)
# In python with flask configuration upon this script made the code syntax a digital pad with 4 buttons like: up, down, left, right, but replace this buttons with: rock, paper, scissors and shuffle
# The shuffle button will be the one that will be used to make the choice of the computer and the other 3 buttons will be used to make the choice of the player
# app.config["SECRET_KEY"] = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
# app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
# app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
# app.config["WIDTH"] = 1100
# app.config["HEIGHT"] = 770

@app.route("/")
def hello():
    return app.send_static_file("index.html")

