from icrawler.builtin import BingImageCrawler


def img_loader():
    crawler = BingImageCrawler(storage={'root_dir': './img'})
    crawler.crawl(keyword="white rose", max_num=5)


def main():
    img_loader()


if __name__ == '__main__':
    main()
