# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Spider, Item


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    url_token = Field()
    name = Field()
    avatar_url = Field()
    type = Field()
    url = Field()
    user_type = Field()
    headline = Field()
    gender = Field()
    vip_info = Field()
    badge = Field()
    follower_count = Field()
    answer_count = Field()
    articles_count = Field()
    employments = Field()



