# -*- coding: utf-8 -*-
import scrapy

from ..items import News


class NewsSpider(scrapy.Spider):
    # name属性用来区分不同的Spider
    name = 'news'
    # 请求的链接不是该域名下的会被过滤
    allowed_domains = ['jwc.ctgu.edu.cn']
    # 爬虫在启动的时候需要爬取的url列表
    start_urls = ['http://jwc.ctgu.edu.cn/news_more.asp?page=1']
    cnt = 0

    def parse(self, response):
        # print(response.text)
        # urls = response.css("#table4 > tbody > tr:nth-child(2) > td > div > font > table > tbody tr")
        # urls = response.css("#table4 tr")
        contents = response.css("#table4 tr")

        # print("获取的原始数据", contents)
        # print("开始遍历获取数据")
        pure_contents = contents[10:len(contents) - 1]
        # print(pure_contents.extract())
        for c in pure_contents:
            # print("原始数据：", )
            # print("第二步筛选：", c.css("*::text").extract())
            res = c.css("*::text").extract()
            # print(str(res))
            item = News()
            item["category"] = res[3]
            item["title"] = res[5].replace(" ", "")
            item["view"] = res[7].replace("\r\n", "").replace(" ", "").replace("阅读:", "")
            item["time"] = res[9].replace("\n", "").replace("(", "").replace(")", "")
            item["url"] = "http://jwc.ctgu.edu.cn/" + c.css("a[target='_blank']::attr(href)").extract_first()
            # print(item)
            yield item


            # for r in res:
            #     print(r)
        #     print("---------------------")
        #     hrefs = c.css("::text")
        #     print(hrefs, len(hrefs))
        # for h in hrefs:
        #     print(h.css("a::text").extract())
        # print(u.extract_first())
        # u.css(".href").extract_first()
        # news = News()
        # news['title'] = u.css("a::text").extract()
        # news['author'] = u.css("a::text").extract_first()
        # yield news
        # next = response.css("page a::attr").extract_first()
        # url = reversed.joinurl(next)
        # yield scrapy.Request(url=url, callback=self.parse)
        # 接受start_urls的请求响应结果
        # 解析响应作进一步处理
        # print(contents[-2].extract())

        # print(response.xpath("//*[@id=\"table4\"]/tbody/tr[2]/td/div/center/font/a[1]"))
        self.cnt = self.cnt + 1
        url = "http://jwc.ctgu.edu.cn/news_more.asp?page={}".format(self.cnt)
        print(url)
        yield scrapy.Request(url=url, callback=self.parse)
        pass
