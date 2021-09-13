# stressberry

pre-requisites
```bash
sudo apt install stress libatlas-base-dev libraspberrypi-bin
sudo usermod -aG video <user>
pip3 install --user stressberry
```

### commands
```bash
# without any thirparty apps
while true; do vcgencmd measure_clock arm; vcgencmd measure_temp; sleep 10; done& stress -c 4 -t 900s

# with stressberry
    # stressberry-run options:
    #    (-n "My Test") = test name, which is used later when plotting 
    #    (-i 300) = 5-minute idle periods before and after
    #    (-d 1800) = 30-minute stress time
    #    (-c 4) = 4-cores
    #    (mytest.out) = the filename for the collected data

stressberry-run -n "My Test" -d 1800 -i 300 -c 4 mytest.out
MPLBACKEND=Agg stressberry-plot mytest.out -f -d 300 -f -l 400 1600 -t 30 90 -o mytest.png --not-transparent

```
