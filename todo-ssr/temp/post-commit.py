import time

def liveness_check():
    while True:
    # Add any custom liveness checks here
    # For simplicity, just print a message
    print('Liveness check: Application is alive')
    time.sleep(5)  # Adjust the sleep time based on your requirements

if __name__ == '__main__':
    liveness_check()
