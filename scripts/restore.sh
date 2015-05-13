#!/usr/bin/env sh
 
# First argument: server_root
# Second argument: fixture name

if [ $# -lt 1 ]; then
  echo "you forgot the server_root dir as first parameter" 1>&2
  exit 1
elif [ $# -lt 2 ]; then
  echo "you forgot the fixture name as second parameter" 1>&2
  exit 1
fi

server_root="$1"
fixture_input="$2"
 

cd "$server_root"

if [ -f "./fixtures/$fixture_input" ] && [ -r "./fixtures/$fixture_input" ]; then
  echo "flush db"
  ./manage.py flush
  echo "restore $fixture_input"
  ./manage.py loaddata "$fixture_input"
else
  echo "invalid fixture '$fixture_input'"
fi
