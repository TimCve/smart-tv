# smart-tv
A DIY smart TV project written with Python & Flask. Able to play YouTube videos through VLC media player. Controlled through sending http POST requests to the web server that will run on the computer which is connected to the TV.

- Initialize a python virtual environment and install the following packages:
```
python-vlc
pafy
youtube-dl
Flask
```
- In there, create an src directory where you will put all the code. Copy and paste the code that you got from GitHub in there.
- initiate the server and send all requests to http://IP_OF_MACHINE:5000/tv/WHATEVER_ROUTE

### current routes

**/videoplayer**
syntax:
```
method: POST
data:
{
  "optype": # either "play", "stop", "pause" or "resume",
  "videoid": # id of youtube video
}
```
