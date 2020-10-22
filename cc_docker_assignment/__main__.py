import sys

from cc_docker_assignment.cc_docker_assignment import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
