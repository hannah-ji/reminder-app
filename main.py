import time
from plyer import notification

if __name__ == "__main__":
    
    while True:
        notification.notify(
            title = "It's time to drink water!",
            message = "Health experts recommend drinking 3.7L a day for men or 2.7L for women.",
            timeout=20
        )
        
        time.sleep(60*60)

        notification.notify(
            title = "Stand up for a minute!",
            message = "Sitting down for too long is unhealthy, take a break or go for a walk!",
            timeout = 30
        
        )
        time.sleep(60*60)
