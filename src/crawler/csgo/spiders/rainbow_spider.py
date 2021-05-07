import scrapy
# from scrapy_splash import SplashRequest 


class R6Spider(scrapy.Spider):
    name = "r6"

    start_urls = [
        'https://steamcommunity.com/app/359550/discussions/',
    ]


    def parse(self, response):
        threads = response.xpath("//*[@class='forum_topic_overlay']")
        next_page = response.xpath("//*[@class='pagebtn']")
        next_page = next_page.xpath(".//@href").extract()[1]
        for thread in threads:

            thread_absolute_link = thread.xpath(".//@href").extract_first()

            yield response.follow(thread_absolute_link,self.parse_thread)

        if(next_page != "#"): 
            yield response.follow(next_page,self.parse)

    
    def parse_thread(self,response):
        comments = response.xpath("//*[@class = 'commentthread_comment_text']")
        if(len(comments)!= 0):
            topic = response.xpath("//*[@class = 'topic']/text()").extract()
            content = response.xpath("//*[@class = 'content']/text()").extract()
            topic =  "".join(topic)
            topic = topic.strip()
            content =  "\n".join(content)
            content = content.strip()

            yield {
                "r6": topic
            }
            yield {
                "r6": content
            }
            for comment in comments:
                text = "".join(comment.xpath(".//text()").extract())
                text = text.strip()

                yield {
                "r6": text
            }
            if('ctp' in response.url):
                next_page = response.url
                number = 0
                for i in range(len(next_page)):
                    if(next_page[i] == '='):
                        number = next_page[i+1:]
                        number = int(number)
                        number = str(number+1)
                        next_page = next_page[:i] + number
                        break
            else:
                next_page = response.url + "?ctp=2"
            yield response.follow(next_page,self.parse_thread)

