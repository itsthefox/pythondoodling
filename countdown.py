import time

countdown = int(input("In seconds, how long is the countdown? "))
print("Counting down from " + str(countdown) +".")
while countdown >= 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)
    if countdown == 0:
        print(countdown)
        print("Countdown complete")
        break