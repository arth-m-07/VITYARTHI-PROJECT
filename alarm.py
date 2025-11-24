import datetime
import time
import pygame
def set_alarm(alarm_time):
    print(f"Alarm set for the time:{alarm_time}")
    sound_file="sound.mp3"
    is_loop = True
    while is_loop:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time==alarm_time:
            print("WAKEY WAKEY! ITS TIME FOR SCHOOL")


            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)


            is_loop = False

        time.sleep(1)

if __name__ == '__main__':

    alarm_time=input("enter the time: HH:MM:SS")
    set_alarm(alarm_time)