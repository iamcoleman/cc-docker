from cc_docker_assignment.cc_docker_assignment import create_result_file, read_result

if __name__ == "__main__":
    # make the '/home/output/result.txt' file
    create_result_file()

    # read and print the contents of 'result.txt'
    read_result()
