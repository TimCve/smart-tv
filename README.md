# smart-tv
A DIY smart TV project

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
