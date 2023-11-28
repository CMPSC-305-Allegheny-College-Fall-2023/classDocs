rem MacOS and Ubuntu container builder and executer
rem https://neo4j.com/developer/docker-run-neo4j/

@echo off
echo This is interactive Neo4j client for your browser
echo  [+]  Use browser address: http://localhost:7474
echo  [+]  Login: neo4j
echo  [+]  Password: password
echo  [+]  To find the containerID: docker ps
echo  [+]  To stop the container: docker stop testneo4j
echo  [+]  To remove the container after stopping it:  docker rm containerID
echo  [+]  Any errors are listed below might be fixed by stopping
echo       and removing the container, and then rerunning ...

# reference: https://voiceofthedba.com/2022/06/06/getting-neo4j-running-in-docker-on-windows/
docker run --name testneo4j -p7474:7474 -p7687:7687 -d -v c:%HOMEPATH%\neo4j\data:/data -v c:%HOMEPATH%\neo4j\logs:/logs -v c:%HOMEPATH%\neo4j\import:/var/lib/neo4j/import -v c:%HOMEPATH%\neo4j\plugins:/plugins --env NEO4J_AUTH=neo4j/password     neo4j:latest

rem Start up the container
docker start testneo4j
rem ref : https://neo4j.com/developer/docker-run-neo4j/#commands-exec
