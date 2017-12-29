# Pixel Traffic: Circle Rush start over and over again

from time import sleep

switchApp("ptcr") # MacOS

maxruns = 1200
runs = 0

while runs < maxruns:
    wait("1514502336053.png",120) # wait for 2 minutes
    click("1514502336053.png")
    
    runs = runs + 1
    sleep(1)