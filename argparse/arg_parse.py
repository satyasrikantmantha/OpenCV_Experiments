import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="Name of the user")
args = vars(ap.parse_args())

print("Hi there {}, it is nice to meet you.".format(args["name"]))