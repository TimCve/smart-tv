#!/usr/bin/env python

import json
from flask import Flask, request, jsonify
import vlc
import threading
import pafy
from time import sleep
import sys
import env

app = Flask(__name__)

API_key = env.api_key

Instance = vlc.Instance()
player = Instance.media_player_new()

# route for playing a video on the tv
@app.route("/tv/videoplayer", methods=["POST"])
def videoplayer():
	operations = ["play", "stop", "pause", "resume"]
	operation = json.loads(request.data)["optype"]

	player.isPaused = False

	def playVideo(playurl):
		# setting up and playing the audio
		Media = Instance.media_new(playurl)
		Media.get_mrl()
		player.set_media(Media)
		player.play()

		sleep(2)
		while player.is_playing() or player.isPaused:
			# print(player.can_pause())
			# print(player.is_playing())
			sleep(0.2)
		player.stop()
		player.isPaused = False

	def execute(op):
		if op == operations[0]:
			player.stop()
			videoUrl = "https://www.youtube.com/watch?v=" + json.loads(request.data)["videoid"]

			# sets up the url for playing with VLC
			video = pafy.new(videoUrl)
			best = video.getbest()
			playurl = best.url

			playerThread = threading.Thread(target=playVideo, args=(playurl,))
			playerThread.start()
		elif op == operations[1]:
			player.stop()
		elif op == operations[2] or op == operations[3]:
			player.pause()
			if player.isPaused:
				player.isPaused = False
			else:
				player.isPaused = True

	if operation in operations:
		execute(operation)

	return json.dumps({"msg": "success!!"})

app.run(host="0.0.0.0", debug=True)
