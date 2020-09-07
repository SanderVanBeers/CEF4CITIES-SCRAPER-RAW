# CEFAT4CITIES Scraper

## Development

### Step 1: Docker

After making changes to the project (i.e. adding classifier models, changing seed list), you are required to rebuild the Docker image.

```
docker build . -t docker.crosslang.com/cefat4cities/scraper
```
After which the docker image can be pushed to the CrossLang docker repo.
```
docker push docker.crosslang.com/cefat4cities/scraper
```

If you are not logged in to the docker repo, you'll need to authenticate first.

```
docker login docker.crosslang.com
```
### Step 2: Kompose

You can convert the docker-compose.yaml to generate a Chart that can be used with Helm using the _-c_ -flag:
```
kompose convert -c
```
Make sure the apiVersion is _apps/v1_ for all .yaml-files in the _docker-compose_-directory.
Each deployment .yaml-files should also contain: 
```yaml
apiVersion: apps/v1
>...
spec:
  replicas: 1
  selector:
    matchLabels:
      io.kompose.service: scraper-xx
```
### Step 3: Helm

Make sure to undo the installation of the previous version (Which we called _scraper_)

```
helm uninstall scraper
```
After uninstalling, run install the new helm by pointing to the directory _docker-compose_ created in step 2. You can choose the installation name, we chose _scraper_.
```
helm install scraper docker-compose
```

## Usage

The directory 'languages' contains the seedlist for the scraper as well as the classifier model used to determine whether the html should be saved or not.
By default the scraper will save all documents indiscriminately in the docs/ subdirectory of the mapped volume.

To create docker image:

```
docker build . -t docker.crosslang.com/cef4cities/scraper
```

To run docker image for a single language:

```
docker run -d -e language={ISO 639-1 language code} --mount source=scraped-data,target=/output cef4cities/scraper
```

## Running the docker-compose will start scrapers for all languages

To build docker-compose images:

```
docker-compose build
```

To run docker-compose:

```
docker-compose up
```

## Troubleshooting

If Rancher gets stuck while deleting the volumes, you may have to delete them manually. In fact you have to delete the pods connected to the volumes.
It's possible Rancher does not show the pods anymore, but using the following commands you can find out if they have actually been deleted succesfully.
```
kubectl get volumeattachments
kubectl get pods
kubectl get rs
```
If they are not, you have to delete the replicasets. You can achieve this by:
```
kubectl delete rs scraper-xx-xxxxxx
```
If that worked, you still have to delete the pods.
```
kubectl delete pod xxxxxxxxx
```
This should remove all volumeattachments. To verify:
```
kubectl get volumeattachments
```
If the previous steps did not remove all volumeattachments, refer to https://ralph.blog.imixs.com/2020/05/28/kubernetes-force-to-delete-volumeattachments/ for further steps.