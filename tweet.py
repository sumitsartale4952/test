import tweepy
import RPi.GPIO as GPIO
import time
import atexit
from dfadc import *
board_detect()
while board.begin() != board.STA_OK:
    print_board_status()
    print("board begin failed")
    time.sleep(2)
print("board begin success")

board.set_adc_enable()

atexit.register(GPIO.cleanup)
GPIO.setmode(GPIO.BCM)
from time import strftime

# Twitter API credentials
consumer_key = 'dPBokzBpT5enq0PzPWKWyZ0uQ'
consumer_secret = 'uH6835UJECBnIzZXUuZU6tqgZFiwaAKhJ28BTu0nmzaJVEB5qD'
access_token = '1685624103699615744-JhiHPJ3aWOV7w2KzQ7c5WM9VVrjpYV'
access_token_secret = 'o15pNnUKXKGg1tHl8gjOwH3W8TO1KlF0ajcktYNwZARD8'

client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,
                       access_token=access_token, access_token_secret=access_token_secret)

location = "JNTU College 📍"  # Adding a location icon

while True:
    # Read sensor values
    temp = board.get_adc_value(board.A0)  # A0 channel read
    humidity = board.get_adc_value(board.A1)
    temperature = (temp / 4096) * 100 + 20  # Calculate temperature
    humidity = (humidity / 4096) * 100  # Calculate humidity

    # Format time and sensor data
    time_stamp = strftime("%d-%m-%y %H:%M:%S", time.localtime())
    temperature_icon = "🌡️"
    humidity_icon = "💧"

    # Create a tweet with emojis and structured formatting
    tweet = (
        f"🏫 Location: {location}\n"
        f"⏰ Time: {time_stamp}\n"
        f"{temperature_icon} Temperature: {temperature:.1f}°C\n"
        f"{humidity_icon} Humidity: {humidity:.1f}%"
    )

    print(tweet)  # Print tweet content to the console for debugging

    # Send the tweet
    client.create_tweet(text=tweet)
    print("Tweet sent to Twitter!")

    # Wait before the next update
    time.sleep(300)  # Wait for 5 minutes (300 seconds)
