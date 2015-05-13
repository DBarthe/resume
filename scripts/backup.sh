#!/usr/bin/env sh
 
# First argument: server_root

if [ $# -lt 1 ]; then
  echo "you forgot the server_root dir as first parameter" 1>&2
  exit 1
fi

server_root="$1"
fixture_output="./fixtures/$(date +"%d-%m-%y-%R-%S").json"

cd "$server_root"
./manage.py dumpdata --natural -e contenttypes -e auth.Permission -o "$fixture_output"

echo "ouput: $fixture_output"
