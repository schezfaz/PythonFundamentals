# thumbnail_maker.py
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve
import threading

import PIL
from PIL import Image

FORMAT = "[%(threadName)s,%(asctiime)s, %(levelname)s] %message()"
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format = FORMAT)

class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        #to get total number of bytes downloaded
        self.downloaded_bytes = 0
        #lock to keep shared variable: downloaded_bytes accurate
        self.dl_lock = threading.Lock()



    def download_image(self,  url):
        #this method will download each image and save it to the input directory
        logging.info("downloading image at URL: " +url)
        img_filename = urlparse(url).path.split('/')[-1]
        dest_path = self.input_dir + os.path.sep + img_filename
        urlretrieve(url, dest_path)

        #moving critical section dealing with shared memory to a with scope of the lock
        #gaurantees that even if current thread gets interrupted, no other thread can modify  the downloaded_bytes variable while it has the lock
        with self.dl_lock:
            img_size = os.path.getsize(dest_path)
        self.downloaded_bytes += img_size #here this value could be corrupted and data could be lost if the thread fails to execute properly, thus we use a lock 
        logging.info("Image [{} bytes ] saved to : {}  ".format(img_size,dest_path))
        
    def download_images(self, img_url_list):
        # validate inputs
        if not img_url_list:
            return
        os.makedirs(self.input_dir, exist_ok=True)
        
        logging.info("beginning image downloads")

        start = time.perf_counter()
        threads = [] #ref. to the thread objects
        for url in img_url_list:
            t= threading.Thread(target=self.download_image, args=(url,))
            t.start()
            # we do not call t.join() here as what would happen in this loop the main thread will create a new thread, start it and then wait for it to complete before proceeding with the loop
            # we want to initiate execution of all worker threads and then wait for them to complete
            threads.append(t)

        for t in threads:
            t.join() #forces main thread to wait for all threads to complete execution
        end = time.perf_counter()

        logging.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))

    def perform_resizing(self):
        # validate inputs
        if not os.listdir(self.input_dir):
            return
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        for filename in os.listdir(self.input_dir):
            orig_img = Image.open(self.input_dir + os.path.sep + filename)
            for basewidth in target_sizes:
                img = orig_img
                # calculate target height of the resized image to maintain the aspect ratio
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                # perform resizing
                img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)
                
                # save the resized image to the output dir with a modified file name 
                new_filename = os.path.splitext(filename)[0] + \
                    '_' + str(basewidth) + os.path.splitext(filename)[1]
                img.save(self.output_dir + os.path.sep + new_filename)

            os.remove(self.input_dir + os.path.sep + filename)
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        self.download_images(img_url_list)
        #self.perform_resizing()

        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))
    