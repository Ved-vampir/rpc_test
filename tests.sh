#!/bin/sh

set -x
test_file="test_res"

rm "json_stat"

./client.py pyro 5 10000 > $test_file
./client.py pyro 100 10000 >> $test_file
./client.py pyro 200 10000 >> $test_file
PORT=39998 ./client.py rpyc 5 40000 >> $test_file
PORT=39998 ./client.py rpyc 100 40000 >> $test_file
PORT=39998 ./client.py rpyc 200 40000 >> $test_file
PORT=8080 ./client.py web 5 40000 >> $test_file
PORT=8080 ./client.py web 100 40000 >> $test_file
PORT=8080 ./client.py web 200 40000 >> $test_file
PORT=39999 ./client.py zmq 200 40000 >> $test_file
PORT=39999 ./client.py zmq 200 40000 >> $test_file
PORT=39999 ./client.py zmq 200 40000 >> $test_file

./avg.py >> $test_file
