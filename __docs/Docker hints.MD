To create a Docker image, you need to follow these steps:

Ensure you have a Dockerfile in your project directory. This file contains the instructions for building the Docker image.

Open a terminal and navigate to the directory containing your Dockerfile.

Run the docker build command to create the image. You can tag the image with a name for easier reference.

Here is the command to build the Docker image:
```sh
docker build -t nuvem-dedupe-app:latest .
```

You can verify that the image was created successfully by running:
```sh
docker images
```

Assuming you have built the Docker image named nuvem-dedupe-app, you can run it with a custom container name like this:
```sh
docker run --name nuvem-dedupe-app nuvem-dedupe-app:latest