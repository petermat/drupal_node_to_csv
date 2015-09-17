# drupal_node_to_csv
simple python 3 script
iterate nodes and save content to csv and save photos from nodes to same folder

Requirements:
1) Install BS4 with pip3 : sudo pip3 install -U beautifulsoup4
2 Install Requests with pip3 : sudo pip3 install -U requests

Usage:
1)Save main.py to folder, rename it if you want

2)Change variables in source code:
  dp_url = "http://yourURL.com/" #set url, https not tested
  dp_node_start = 1 #first node in drupal iteration
  dp_node_end = 3010 #last node in drupal iteration

3) start script:
  python3 main.py

