import requests
import time


def slowgetter():
    start = time.time()

    for i in range(1, 33):
        url = 'https://data.cyber.org.il/os/demo/movie{0}.txt'.format(i)
        r = requests.get(url, allow_redirects=True)
        open('movie{0}.txt'.format(i), 'wb').write(r.content)
        file = open('movie{0}.txt'.format(i), 'r')
        print("movie number {0} -".format(i), file.read())

    end = time.time()
    print(end - start)

if __name__ == '__main__':
    slowgetter()