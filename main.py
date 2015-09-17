#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import socket
import csv

# Install BS4 with pip3 : sudo pip3 install -U beautifulsoup4
from bs4 import BeautifulSoup
# Install Requests with pip3 : sudo pip3 install -U requests
import urllib.request
from urllib.request import urlretrieve
import http.client
from datetime import datetime


# VARIABLES
dp_url = "http://www.yourURL.com/"  # set url, https not tested
dp_node_start = 1  # first node in drupal
dp_node_end = 3010  # last node in drupal


# translate name of months to English, use your language if needed
def translateDate(date):
    date = date.replace("Január", "January")
    date = date.replace("Február", "February")
    date = date.replace("Marec", "March")
    date = date.replace("Apríl", "April")
    date = date.replace("Máj", "May")
    date = date.replace("Jún", "June")
    date = date.replace("Júl", "July")
    date = date.replace("Október", "October")
    # date = date.replace("Jún", "June")
    # date = date.replace("Jún", "June")

    return date


if __name__ == '__main__':


    # main iteration loop for node range defined in variables
    for node_iterator in range(dp_node_start, dp_node_end+1):  # +1 because range ends in dp_node_end-1
        url_iterator = dp_url + "node/" + str(node_iterator)

        # urllib request
        try:
            req = urllib.request.Request(url_iterator, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)

            checksoup = BeautifulSoup(response.read(), "html.parser")

            title = checksoup.find('h1', class_='title').text.replace("\n", "")

            try:
                submitted = checksoup.find('div', class_='submitted').text.replace("\n", "")
                autor = submitted.split(",")[0]
            except:
                autor = None
                pass


            date = ",".join(submitted.split(",")[1:])
            date = date.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "").strip()
            # date = "April 1, 2001"
            date = translateDate(date)

            try:
                date_unixtimestamp = datetime.strptime(date, '%B %d, %Y')
                date_unixtimestamp = date_unixtimestamp.strftime('%s')
            except:
                date_unixtimestamp = None
                pass

            # beautifulsoup4 finds elements on downloaded page
            taxonomy = checksoup.find('div', class_='taxonomy')  # .text.replace("\n", "")
            content = checksoup.find('div', class_='content')  # .text.replace("\n", "")
            images = checksoup.find('div', class_='content').findAll('img')

            # loop for donloading images
            images_names = []
            for image in images:
                imageurl = image.get('src')
                imagename = (image.get('src').split("/")[-1:][0])
                print("\nimagename:", imagename,
                    "\nimageurl: ", imageurl)
                    # ,"\nimagepath: ", imagepath)

                try:
                    urlretrieve(imageurl, imagename)
                    images_names.append(imagename)
                except:
                    print("*** urlretrieve error: ", imageurl)

            # print for debug
            print(url_iterator,
                  "\nTitle:", title,
                  "\nAuthor:", autor,
                  "\nDate:", date,
                  "\ndate_unixtimestamp:", date_unixtimestamp,
                  # "\nContent", content,
                  "\nImages:", images,
                  "\ntaxonomy:", taxonomy,
                  "\n\n")

            # WRITE TO CSV #
            # csv_filename = os.path.join(os.getcwd()+"/csv/" + title +".csv")  # safer version
            csv_row = [node_iterator, url_iterator, title, autor, date, date_unixtimestamp, images_names, taxonomy, content]

            csv_filename = "output_nodes.csv"
            if not os.path.exists(csv_filename):
                with open(csv_filename, 'wt') as csv_file:
                    writer = csv.writer(csv_file, delimiter=';')
                    writer.writerow(csv_row)

            else:
                with open(csv_filename, "a", newline='') as csv_file:
                    writer = csv.writer(csv_file, delimiter='|', quoting=csv.QUOTE_ALL)
                    writer.writerow(csv_row)

        except (urllib.error.HTTPError, socket.error, socket.gaierror, http.client.BadStatusLine) as err:
            print(url_iterator, err.code, "\n")

        except (urllib.error.URLError) as err:
            print(url_iterator, str(err), "\n")

        except (AttributeError, TypeError, ValueError, SystemError) as err:
            print(url_iterator, str(err), "\n")

        time.sleep(1)
