import random
import time

def read_sensor_data():
    return {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 60.0), 2),
        "timestamp": time.time()
    }

if __name__ == "__main__":
    while True:
        print(read_sensor_data())
        time.sleep(1)
