# -*- coding: utf-8 -*-
from requests import get
from bs4 import BeautifulSoup


def best_hashtags(tag, kind='popular'):
    r = get(f'http://best-hashtags.com/hashtag/{tag}/')
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        tag_boxs = soup.findAll("div", {"class": "tag-box"})

        if len(tag_boxs) == 0:
            return []

        n = ['popular', 'liked'].index(kind)

        if n == -1:
            n = 0

        tags = tag_boxs[n].get_text()
        return [s.strip(' #') for s in tags.split()]


def ritetag(tag):
    r = get(f'https://ritetag.com/best-hashtags-for/{tag}')
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        tags = soup.findAll("a", {"class": "good"})
        result = []
        for tag in tags:
            s = tag.get_text()
            if s.find('#') != -1:
                result.append(s.strip(' #'))

        return result


def instatag(tag):
    r = get(f'http://instatag.net/{tag}.html')
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        tags = soup.find("textarea", {"id": "note"}).get_text()
        return [s.strip(' #') for s in tags.split()]


def displaypurposes(tag):
    r = get(f'https://d212rkvo8t62el.cloudfront.net/tag/{tag}')
    if r.status_code == 200:
        data = r.json()
        return [s['tag'] for s in data.get('results', [])]
