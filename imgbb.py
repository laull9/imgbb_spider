from page_img_spider import *
import re
from lxml.etree import HTML
import requests


class IMGBB_SPIDER(Page_img_spider):
    def __init__(self, url: str):
        print("解析页面...")
        url = re.findall(r"https://ibb\.co/album/\w{5,8}|https://.*?\.imgbb\.com", url)[0]
        if url.endswith(".com"):
            url += "/"
        if not url.endswith("?sort=name_asc&page=1"):
            url += "?sort=name_asc&page=1"
        img_urls = []
        hang_count = 1
        while True:
            try:
                # print(f"url -- {url}")
                res = requests.get(url, headers=random_header()).text
                img_urls.extend(re.findall(r"https://ibb.co/\w{7,8}", res)[::2])
                h = HTML(res)
                if not self.dirpath:
                    __name = h.xpath("/html/body/div[1]/div[3]/h1/a/text()")  # album
                    if not __name:
                        __name = h.xpath("/html/body/div[1]/div[1]/div[1]/h1/a/text()")  # 个人
                    if not __name:
                        __name = ["未知的标题"]
                    self.dirpath = "./" + __name[0]
                url = h.xpath("/html/body/div[1]/div/div/div[4]/ul/li[3]/a/@href")[0]
                print(f"\r解析了{hang_count}页    ", end="")
                hang_count += 1
            except:
                break
        count = 0
        for img_url in img_urls:
            count += 1
            self.img_name_s.append( (img_url, f"{count}") )
        self.all_count = count
        img_urls.clear()
        print(f"开始下载, 标题--{self.dirpath[2:]}, 共{count}个")

    @staticmethod
    def reget_img(img_url):
        res_ = requests.get(img_url, headers=random_header()).text
        return HTML(res_).xpath("/html/head/link[11]/@href")[0]


if __name__ == '__main__':
    print("作者@laull9\n根据imgbb图床的相册或者个人主页爬取【高清原图】\n会下载到程序所在的文件夹")
    print("关于如何找图集，在Bing(必应搜索 https://cn.bing.com/)\n搜索：[你要搜的] site:ibb.co\n比如搜索：甘雨 site:ibb.co")
    try:
        url = input("\n输入imgbb 网址>>>")
        IMGBB_SPIDER(url).run()
    except:
        print("输入错误")