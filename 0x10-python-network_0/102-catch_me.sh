#!/bin/bash
# secauses the server to respond with a message
curl -sLX PUT "You got me!" -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
