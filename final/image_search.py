#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:41:01 2020

@author: mitalijuneja1
"""

import requests, io, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image


def get_image_url(search_term):
    search_term = format_search_term(search_term)
    search_url = 'https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img'
    search_url = search_url.format(q = search_term)
    image_url = ''
    wd = webdriver.Chrome(ChromeDriverManager().install())
    wd.minimize_window()
    wd.get(search_url)
    results = wd.find_elements_by_css_selector('img.Q4LuWd')
    for thumbnail in results:
        try:
            thumbnail.click()
            time.sleep(1)
            break
        except Exception:
            continue
    images = wd.find_elements_by_css_selector('img.n3VNCb')
    for image in images:
        if image.get_attribute('src') and 'http' in image.get_attribute('src'):
            image_url = image.get_attribute('src')
            try:
                save_image(image_url)
                break
            except Exception:
                continue
    wd.close()


def save_image(image_url):
    image_content = requests.get(image_url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert('RGB')
    file_path = 'static/city.jpg'
    with open(file_path, 'wb') as f:
        image.save(f, "JPEG", quality=95)
        
  
def format_search_term(search_term):
    term_words = search_term.split()
    term_words.append('beautiful')
    term_words.append('landscape')
    return '+'.join(term_words)



