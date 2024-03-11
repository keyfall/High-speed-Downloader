import os, subprocess

magnet_link = "magnet:?xt=urn:btih:C168B7AD1413C99338EAEFA9C1A0E781F27D3072"
trackers = []
with open("trackers_best.txt", "r") as file:
    for tracker in file:
        trackers.append(tracker.strip())
trackers_str = ",".join(trackers)

print(trackers_str)
# command = 'aria2c --bt-tracker=$trackers_str $magnet_link"'
# output = subprocess.check_output(command, shell=True, text=True)
# print(output)