import scrapy

class GoogletrendsSpider(scrapy.Spider):
    name = "GoogleTrends"
    allowed_domains = ["trends.google.com"]
    start_urls = ["https://trends.google.com/trends/explore?date=2022-01-01%202022-12-31&geo=US&q=covid"]

    def parse(self, response):

        data = open("covid_interest_2023.txt", "w")

        x_path = "//div[@aria-label='A tabular representation of the data in the chart.']/table/tr"
        table = response.xpath(x_path)
        rows = table.xpath("//tr")
        for row in rows:
            data.write(str(row.xpath("//td[0]/text()").extract()) + " - ")
            data.write(str(row.xpath("//td[1]/text()").extract()) + "\n")

        data.close()