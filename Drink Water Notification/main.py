from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "***Time to drink Water!***",
            message = "You are not hungry, you are just bored.Drink a glass of water and learn the difference.",
            timeout = 10,
            app_icon = "/home/emarti/Downloads/Python Projects/Drink Water Notification/glass.png"
        )
        time.sleep(60*60)