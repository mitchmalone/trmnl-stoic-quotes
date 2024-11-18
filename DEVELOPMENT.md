# Development Notes

## Test Locally

```bash
# Build the docker image
docker build -t hello-world .

# Run the container
docker run -p 8080:8080 hello-world

# Navigate to http://localhost:8080
```