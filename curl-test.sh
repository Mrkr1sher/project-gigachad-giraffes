#!/usr/bin/bash
NAME="Krish"
EMAIL="krishthawani46@gmail.com"
CONTENT="Testing Curl Bash Script!"

curl http://localhost:5000/api/timeline_post # should be an empty

curl -X POST http://localhost:5000/api/timeline_post -d "name=$NAME&email=$EMAIL&content=$CONTENT"

curl http://localhost:5000/api/timeline_post # should contain the entry
