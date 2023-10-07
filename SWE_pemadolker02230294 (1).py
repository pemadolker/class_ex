#I did make use of chatgpt but didnt copy the code directly or without understanding 
import pygame
import time
import moviepy.editor as mp
from plyer import notification
import psutil
from datetime import datetime

original_video_file = r"C:\Users\DELL\Desktop\stay.mp4"

scheduled_time = "22:00"

scheduled_time_parts = scheduled_time.split(":")
scheduled_seconds = int(scheduled_time_parts[0]) * 3600 + int(scheduled_time_parts[1]) * 60

current_time = time.localtime()
current_seconds = current_time.tm_hour * 3600 + current_time.tm_min * 60 + current_time.tm_sec

time_delay = scheduled_seconds - current_seconds

if time_delay > 0:
    print(f"Waiting for {time_delay} seconds until {scheduled_time}...")
    time.sleep(time_delay)

pygame.init()

screen_info = pygame.display.Info() 

window_width =  screen_info.current_w
window_height = screen_info.current_h
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("I'M CERTAIN THAT HE IS AN ANGEL-_-")

video = mp.VideoFileClip(original_video_file)

video.preview()

start_time = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    elapsed_time = time.time() - start_time

    if elapsed_time > video.duration:
        font = pygame.font.Font(None, 36)
        text = font.render("Video Finished!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()

def run_laptop_usage_alert():
    max_usage_duration =3600
    while True:
        laptop_usage = psutil.sensors_battery().secsleft

        if laptop_usage >= max_usage_duration:
           message = "It's time to take a break from your laptop!"
           
           notification.notify(
            title="Laptop Usage Alert",
            message=message,
            app_name="LaptopUsageAlert",
            timeout=10,
           )
           break

    time.sleep(3600)  
if __name__ == "__main__":
    run_laptop_usage_alert()
