#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Date    : 2017-11-11 21:07:43
@Author  : Liao Jiabin
'''

import scrapy
from ..items import ZufangItem


class GanjiSpider(scrapy.Spider):
    '''
    get house data from ganji.com
    '''

    name = 'zufang'
    start_urls = ['http://bj.ganji.com/fang1/chaoyang/', ]

    def parse(self, response):
        print(response)
        zf = ZufangItem()
        title_list = response.xpath(
            ".//div[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        money_list = response.xpath(
            ".//div[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()

        for i, j in zip(title_list, money_list):
            zf['title'] = i
            zf['money'] = j
            yield zf
            # print(i, ':', j)
