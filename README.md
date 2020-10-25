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
    - Where `<your_file_location>` is the path to a directory on your computer that contains the `.txt` files you want to analyze
2. This will create and run the Docker container `cc-docker-container`
3. The contents of the generated `result.txt` file will be displayed in your console


### View file structure of the container
1. Run the command `docker export -o <file_name>.tar cc-docker-container`
    - where `<file_name>` is any name you choose
2. This will create a `.tar` file in your current directory. You can open this `.tar` file to see the file structure of the container.
    - Application files are located in `/home/app`
    - The directory you specify when running the container is bound to `/home/data`
    - The `result.txt` file is saved to `/home/output`
    

### Example Run
1. I have included some `.txt` files used for testing in the `/hold/text-files` folder.
2. I have included a `/hold/example_file_structure.tar` file that is a result of running the `docker export` command on the `cc-docker-container` after running the application against the text files that I mentioned above.
