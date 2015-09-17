# drupal_node_to_csv
Simple python 3 script Iterate Drupal nodes and save content to csv and save photos from nodes to same folder

Script grabs content of div elements. you can add more elements or edit these ones:

- Variable submitted grabs div or author and published date. Unix timestamp is derived from published date to get universal time.
  
  `submitted = checksoup.find('div', class_='submitted').text.replace("\n", "")`

  `autor = submitted.split(",")[0]`

  `date = ",".join(submitted.split(",")[1:])`

  `date_unixtimestamp = datetime.strptime(date, '%B %d, %Y')`

  `date_unixtimestamp = date_unixtimestamp.strftime('%s')`
- Taxonomy variable drom taxonomy div      

  `taxonomy = checksoup.find('div', class_='taxonomy')`

- Main content div

  `content = checksoup.find('div', class_='content')`

- Images find all images in main content

  `images = checksoup.find('div', class_='content').findAll('img')`


##Requirements:

1.**Install BS4 with pip3:**

`sudo pip3 install -U beautifulsoup4`


2.**Install Requests with pip3:**

`sudo pip3 install -U requests`




##Usage:

1. **Save main.py to folder**, rename it if you want
2. **Change variables in source code:**

  `dp_url = "***http://yourURL.com/***" #set url, https not tested`

  `dp_node_start = **1** #first node in drupal iteration`

  `dp_node_end = **3010** #last node in drupal iteration`

3. **Run script**:
  
  `python3 main.py`

