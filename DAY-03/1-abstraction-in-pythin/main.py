import sys

# the real way
sys.stdout.write("Enter something :")
sys.stdout.flush()
value = sys.stdin.readline()
sys.stdout.write(value + "\n")


