# Intro
> This mini-project basically pulls data from the EBird project via its API, stores it into this local database, and then outputs some of the info to the screen. The EBird project stores data about bird observations made all over the world (mainly the Anglophone world I believe). An individual observation record inlcudes the observed bird's common & scientific name, the location of the observation, the observer's distance from the creature, region, time, date, and other info. 
## Setup instructions
* libraries: requests (for API requests), sqalchemy, pandas (for database)
* install & run: just download the project and run it from your terminal
  * ('python birds.py)
  * output will be the 10 latest bird observations
## Code overview
* birds.py: calls the EBird API, grabs data, stores it in our local database, and prints observations
* bird_database.db: the SQL database where we store the observations (there are a *LOT*)
* Output: The default is to only output the first 10 latest observations but you can change the SQL query in birds.py

Link to the EBird API used in this project:
https://documenter.getpostman.com/view/664302/S1ENwy59

![Example Workflow](https://github.com/Galarcel/eBird-API-Project/actions/workflows/stylecheck.yaml/badge.svg)
![Example Workflow 2](https://github.com/Galarcel/eBird-API-Project/actions/workflows/unittests.yaml/badge.svg)

