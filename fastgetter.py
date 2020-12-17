import requests
import time
import threading
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def worker(i):
    # get movie from url
    url = 'https://data.cyber.org.il/os/demo/movie{0}.txt'.format(i)
    r = requests.get(url, allow_redirects=True)
    
    # save movie in file
    open('movie{0}.txt'.format(i), 'wb').write(r.content)
    
    file = open('movie{0}.txt'.format(i), 'r')

    # printing using logging
    logging.info("movie number {0} - {1}".format(i, file.read()))


def fastgetter():
    threads = []
    start = time.time()

    # creats threads
    for i in range(1, 33):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    # waits for all threads to finish
    for i in threads:
        i.join()
        
    end = time.time()
    logging.info("time:{}".format(end - start))


if __name__ == "__main__":
    fastgetter()
