from ast import Or


LOOPS = int(input('How many times did you go around the track? '));
LAP_SUM = 0;
CURRENT_TIME = 0
FASTEST_TIME = 0;
SLOWEST_TIME = 0;

for counter in range(LOOPS):
    LAP_TIME = float(input('Lap time: '))
    LAP_SUM += LAP_TIME;

    if LAP_TIME < FASTEST_TIME or FASTEST_TIME == 0:
        FASTEST_TIME = LAP_TIME; 

    if LAP_TIME > SLOWEST_TIME:
        SLOWEST_TIME = LAP_TIME; 

print('Average Lap Time: ' + str(LAP_SUM/LOOPS));
print('Fastest Lap Time: ' + str(FASTEST_TIME));
print('Slowest Lap Time: ' + str(SLOWEST_TIME));