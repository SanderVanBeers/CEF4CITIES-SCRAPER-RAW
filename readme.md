# CEFAT4CITIES Scraper

## Usage

The directory 'languages' contains the seedlist for the scraper as well as the classifier model used to determine whether the html should be saved or not.
By default the scraper will save all documents indiscriminately in the docs/ subdirectory of the mapped volume.

To create docker image:
docker build . -t cef4cities/scraper

To run docker image:
docker run -d -e language={ISO 639-1 language code} --mount source=scraped-data,target=/output cef4cities/scraper

## Running the docker-compose will start scrapers for all languages

To build docker-compose images:
docker-compose build

To run docker-compose:
docker-compose up
