
#########
# Mitali Juneja (mj2944)
# Final assignment = image web scraper to find a background image for the
# weather page
#
#########

import requests, io, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image


def get_image_url(search_term):
    """use the input city name to scrape google images for a suitable
    background image"""
    
    # format the query
    search_term = format_search_term(search_term)
    search_url = 'https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img'
    search_url = search_url.format(q = search_term)
    image_url = ''
    # open and minimize the searching window, search for the input query
    wd = webdriver.Chrome(ChromeDriverManager().install())
    wd.minimize_window()
    wd.get(search_url)
    # go through the queries to find a clickable image
    results = wd.find_elements_by_css_selector('img.Q4LuWd')
    for thumbnail in results:
        try:
            thumbnail.click()
            time.sleep(1)
            break
        except Exception:
            continue
    images = wd.find_elements_by_css_selector('img.n3VNCb')
    # try to find an image that is saveable and save it
    for image in images:
        if image.get_attribute('src') and 'http' in image.get_attribute('src'):
            image_url = image.get_attribute('src')
            try:
                save_image(image_url)
                break
            except Exception:
                continue
    # close the window
    wd.close()


def save_image(image_url):
    """save the image that is found"""
    
    image_content = requests.get(image_url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert('RGB')
    file_path = 'static/city.jpg'
    with open(file_path, 'wb') as f:
        image.save(f, "JPEG", quality=95)
        
  
def format_search_term(search_term):
    """format the query for searching"""
    
    term_words = search_term.split()
    term_words.append('beautiful')
    term_words.append('landscape')
    return '+'.join(term_words)



