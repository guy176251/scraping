import os
import asyncio
import aiohttp
import requests
from random import choice
from lxml.html import fromstring
from urllib.parse import unquote
from requests.models import Response
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup as Soup, SoupStrainer as Filter


from lxml.html import HtmlElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


try:
    from .random_headers import random_headers, random_agents
    from .chrome import get_browser
except:
    from random_headers import random_headers, random_agents
    from chrome import get_browser


def get(url) -> Response:
    return requests.get(url, headers=random_headers())


def souper(url, **kwargs):
    return Soup(get(url).content, 'lxml', **kwargs)


def first_elem(e, css):
    if type(e) == WebDriver or type(e) == WebElement:
        try:
            return e.find_element_by_css_selector(css)
        except:
            return None
    elif type(e) == HtmlElement:
        return e.cssselect(css)[0] if e.cssselect(css) else None


def all_elems(e, css):
    if type(e) == WebDriver or type(e) == WebElement:
        return e.find_elements_by_css_selector(css)
    elif type(e) == HtmlElement:
        return e.cssselect(css)


def click(browser, elem_to_move_to, elem_to_click=None, *, pause=0.5):

    if type(elem_to_move_to) == str:
        elem_to_move_to = first_elem(browser, elem_to_move_to)

    if not elem_to_move_to:
        return

    (ActionChains(browser)
     .move_to_element(elem_to_move_to)
     .pause(pause)
     .click(elem_to_click or elem_to_move_to)
     .perform())


def lxmler(url) -> HtmlElement:
    return fromstring(get(url).content)


def get_all(urls) -> list:
    '''Returns response objects from a list of site URLs.'''
    return asyncio.run(get_all_pages(urls))


async def get_all_pages(urls):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[session.get(url, headers=random_headers())
                                         for url in urls])
    return results


# async def get_each_page(session, url, byte):
#     async with session.get(url, headers=random_headers()) as resp:
#         if resp.status == 200:
#             if byte:
#                 page = await resp.read()
#             else:
#                 page = await resp.text()
#             return page
#         else:
#             return None


#if __name__ == '__main__':
#    from discord import Webhook, RequestsWebhookAdapter
#
#    webhook = Webhook.from_url(os.environ['TEST_WEBHOOK'],
#                               adapter=RequestsWebhookAdapter())
#    print('Locals:\n - ' + '\n - '.join(n for n in locals().keys()
#                                        if not n.startswith('_')))
