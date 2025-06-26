# Development Notes

## Test Locally

```bash
# Build the docker image
docker build -t [IMAGE_NAME] .

# Run the container
docker run -p 8080:8080 [IMAGE_NAME]

# Navigate to http://localhost:8080
```

## Deployment

- Using Google Cloud Run
	- Cloud Run Admin API
	- Cloud Build API
	- Container Registry API
- Google Cloud CLI (google-cloud-cli in ArchLinux User Repository)

```bash
gcloud auth login
gcloud config set project [PROJECT_ID]
gcloud auth configure-docker
gcloud services enable containerregistry.googleapis.com
docker tag [SERVICE_NAME] gcr.io/[PROJECT_ID]/[IMAGE_NAME]:latest
docker push gcr.io/[PROJECT_ID/[IMAGE_NAME]:latest
gcloud run deploy [SERVICE_NAME] --image gcr.io/[PROJECT_ID]/[IMAGE_NAME] --platform managed --region us-east1 --allow-unauthenticated
```

## TRMNL Settings

### Markup

```html
<div class="layout">
  <div class="columns">
    <div class="column">
      <div class="markdown gap--large">
        <span style="font-size: 20px;">{{text}}</span>
        <span style="font-size: 16px;">{{author}}</span>
      </div>
    </div>
  </div>
</div>

<div class="title_bar">
  <span class="title">Inspiration</span>
  <span class="instance">Quote of the day</span>
</div>
```

### Settings

- Strategy: Polling
- Polling URL: [FROM GOOGLE RUN DEPLOYMENT]


