# Cloud Computing - Docker Assignment

This small Python application will:
- Read every `.txt` file in a directory on your machine and output all the file names, how many words belong to each file, the total number of words in all files, and which file has the largest number of words.
- Find the IP address of the container
- Save the above two points to a file on the container in `/home/output/result.txt`
- Read from `/home/output/result.txt` and print its contents


### To build the Docker image
1. Navigate to the main `cc-docker/` folder
2. Run `docker build -t cc-docker-image .`
3. This will create the image `cc-docker-image` from the Dockerfile


### To run the Docker image
1. Run the command `docker run
-v <your_file_location>:/home/data
--name cc-docker-container
cc-docker-image` 
    - Where `<your_file_location>` is the path to a directory on your computer than contains the `.txt` files
2. This will create and run the Docker container `cc-docker-container`
3. The contents of the generated `result.txt` file will be displayed in your console
