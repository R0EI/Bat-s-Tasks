#!/bin/bash

API_BASE_URL="15.236.43.194"
touch score.txt

response=$(curl -s -o /dev/null -w "%{http_code}" $API_BASE_URL/tasks)
RESPONSES+=("$response") 
if [[ $response == *"200"* ]]; then 
  echo "GET Request to /tasks was successful." >> score.txt
else
  echo "GET Request to /tasks failed." >> score.txt
fi

response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/x-www-form-urlencoded" --data "task=Test&until=Test&urgency_lvl=C" $API_BASE_URL/task)
RESPONSES+=("$response") 
if [[ $response == *"200"* ]] || [[ $response == *"302"* ]]; then 
  echo "POST Request to /task was successful." >> score.txt
else
  echo "POST Request to /task failed." >> score.txt
fi

response=$(curl -s -o /dev/null -w "%{http_code}" $API_BASE_URL/sorted_tasks)
RESPONSES+=("$response") 
if [[ $response == *"200"* ]]; then
  echo "GET Request to /sorted_tasks was successful." >> score.txt
else
  echo "GET Request to /sorted_tasks failed." >> score.txt
fi  

ID=$(curl -s $API_BASE_URL/id_for_testing)

response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/x-www-form-urlencoded" --data "task=Test&id=$ID" $API_BASE_URL/update_task)
RESPONSES+=("$response") 
if [[ $response == *"200"* ]] || [[ $response == *"302"* ]]; then 
  echo "PUT Request to /task/$ID was successful." >> score.txt
else
  echo "PUT Request to /task/$ID failed." >> score.txt
fi  

response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/x-www-form-urlencoded" --data "id=$ID" $API_BASE_URL/delete_task)
RESPONSES+=("$response") 
if [[ $response == *"200"* ]] || [[ $response == *"302"* ]]; then 
  echo "DELETE Request to /task/$ID was successful." >> score.txt
else
  echo "DELETE Request to /task/$ID failed." >> score.txt
fi  

for item in "${RESPONSES[@]}"; do
  if [[ $item == 200 ]] || [[ $item == *"302"* ]]; then 
    continue
  else
    echo "Test Failed"
    exit 1
  fi
done
