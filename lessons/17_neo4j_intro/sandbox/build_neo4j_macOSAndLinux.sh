#!/bin/bash
# MacOS and Ubuntu container builder and executer
# Formatting
GREEN='\033[0;32m'			# Green
BIGreen='\033[1;92m'		# Green
BICyan='\033[1;96m'			# Cyan
BIRed='\033[1;91m'				# Red
BIYellow='\033[1;93m'     # Yellow
NC='\033[0m' # No Colour

# https://neo4j.com/developer/docker-run-neo4j/


printf "  [+]  ${BIGreen} This is interactive Neo4j client for your browser${NC}\n\n"
printf "  [+]  ${BIGreen} Use browser address: http://localhost:7474${NC}\n"
printf "  [+]  ${BIGreen} Login: ${BIYellow}neo4j${NC}\n"
printf "  [+]  ${BIGreen} Password: ${BIYellow}password${NC}\n\n"
printf "  [+]  ${BIGreen} To find the containerID: ${BICyan}sudo docker ps ${NC}\n"
printf "  [+]  ${BIGreen} To stop the container: ${BICyan}sudo docker stop testneo4j${NC}\n"
printf "  [+]  ${BIGreen} To remove the container after stopping it: ${BICyan}sudo docker rm <containerID>${NC}\n\n"
printf "       ${BIGreen} Any errors are listed below might be fixed by stopping\n        and removing the container, and then rerunning ... ${NC}\n"
printf "\n ${BIRed}"

# Reference: https://neo4j.com/developer/docker-run-neo4j/
sudo docker run \
    --name testneo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -v $HOME/neo4j/import:/var/lib/neo4j/import \
    -v $HOME/neo4j/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/password \
    neo4j:latest

# The following line starts up the container
sudo docker start testneo4j
