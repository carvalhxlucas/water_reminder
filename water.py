import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Drink Water Now!",
            message="Let's keep our body hydrated",
            timeout=10
            )
        time.sleep (60*30)
