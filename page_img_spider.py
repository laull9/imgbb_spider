from concurrent.futures import ThreadPoolExecutor
import tqdm
import func_timeout
import os
from time import sleep
import urllib.request
import random


headers_ = [{'User-Agent': 'Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint;PPC-i830; PPC; 240x320)',
            'Accept-Language': 'fa', 'Referer': 'http://arnold.com/', 'Connection': 'keep-alive'},
           {'User-Agent': 'Opera/7.0 (Windows NT 5.1; U)  [en]', 'Accept-Language': 'or',
            'Referer': 'https://www.nelson.com/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)',
               'Accept-Language': 'lt', 'Referer': 'http://flores.com/', 'Connection': 'keep-alive'},
           {'User-Agent': 'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6',
            'Accept-Language': 'hak', 'Referer': 'https://cantrell.info/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
               'Accept-Language': 'lt', 'Referer': 'https://sims.com/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/525.13.',
               'Accept-Language': 'ms', 'Referer': 'http://www.taylor-cordova.com/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931',
               'Accept-Language': 'lt', 'Referer': 'https://bauer-wagner.biz/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (Macintosh; U; Mac OS X 10_5_7; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5',
               'Accept-Language': 'bs', 'Referer': 'http://www.wright-hicks.com/', 'Connection': 'keep-alive'},
           {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.10) Gecko/20051111 Firefox/1.0.6',
            'Accept-Language': 'lt', 'Referer': 'https://villegas.com/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.422.0 Safari/534.1',
               'Accept-Language': 'mr', 'Referer': 'http://www.cunningham.com/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.10) Gecko/20071126 Ubuntu/7.10 (gutsy) Firefox/2.0.0.10',
               'Accept-Language': 'sl', 'Referer': 'https://simpson.biz/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)',
               'Accept-Language': 'nr', 'Referer': 'http://mccullough.com/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
               'Accept-Language': 'nl', 'Referer': 'http://young-hansen.com/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
               'Accept-Language': 'fur', 'Referer': 'http://higgins-johnson.com/', 'Connection': 'keep-alive'},
           {'User-Agent': 'Opera/9.10 (Windows NT 5.1; U; zh-tw)', 'Accept-Language': 'tig',
            'Referer': 'http://brown-cruz.biz/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13 (.NET CLR 3.5.30729)',
               'Accept-Language': 'da', 'Referer': 'https://www.golden.biz/', 'Connection': 'keep-alive'},
           {'User-Agent': 'Opera/9.10 (Windows NT 5.1; U; MEGAUPLOAD 1.0; pl)', 'Accept-Language': 'id',
            'Referer': 'https://www.patterson.org/', 'Connection': 'keep-alive'},
           {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 5.12  [de]',
            'Accept-Language': 'om', 'Referer': 'https://www.hinton-kent.com/', 'Connection': 'keep-alive'}, {
               'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3; hu-hu) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.1 Safari/525.20',
               'Accept-Language': 'fr', 'Referer': 'http://castillo.com/', 'Connection': 'keep-alive'},
           {'User-Agent': 'Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6',
            'Accept-Language': 'ff', 'Referer': 'http://young.biz/', 'Connection': 'keep-alive'}]


def random_header():
    return random.choice(headers_)

def random_user_agent():
    return random_header()['User-Agent']

def download_item(item_url1: str, save_path1: str):
    """
    :param item_url1: 想要下载的图片网址
    :param save_path1: 想要保存的文件夹路径+保存的文件名，如'C:\\Users\\57795\\Desktop\\Python\\1.jpg'
    :return:
    """
    # 创建一个请求对象
    req = urllib.request.Request(item_url1)
    # 添加请求头
    req.add_header('User-Agent', random_user_agent())
    # 打开 URL
    with urllib.request.urlopen(req) as response:
        # 读取请求内容
        image_content = response.read()
        # 下载并保存
        with open(save_path1, 'wb') as f:
            f.write(image_content)
            f.flush()


def url_tidy(url : str):
    url = url.replace("|", "")
    if url[-1] == "/":
        return url[:-1]
    else:
        return url

def resure_dirpath(dirpath):
    if len(dirpath) > 259:
        dirpath = dirpath[:259]
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath

def remove_empty_dirs(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            # 检查文件夹是否为空
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"移除了空文件夹: {dir_path}")


def desktop_path():
    return os.path.join(os.path.expanduser('~'), "Desktop")


class Page_img_spider:
    THREAD_NUM = 8
    IMG_DOWNLOAD_MAX_FAILED = 5
    IMG_DOWNLOAD_TIME_OUT = 1000

    url, dirpath = "", ""
    img_name_s = []  # 设计为 元组（url， img名字-不带拓展名）
    pool = ThreadPoolExecutor(THREAD_NUM)
    success_count = 0
    failed_count = 0
    failed_urls = []

    def __del__(self):
        self.img_name_s.clear()
        self.failed_urls.clear()

    def run(self):
        self.dirpath = url_tidy(self.dirpath)
        self.dirpath = self.dirpath.replace("\\", "/")
        resure_dirpath(self.dirpath)
        self.all_count = len(self.img_name_s)
        for i in self.img_name_s:
            self.pool.submit(self.download_img, i)
        t = tqdm.tqdm(total=self.all_count, unit="图片/视频", leave=False, maxinterval=0.5)

        now_tqdm = 0
        while self.success_count + self.failed_count < self.all_count:
            up = self.success_count - now_tqdm
            if up:
                now_tqdm = self.success_count
                t.update(up)
            sleep(0.1)
        for i in self.failed_urls:
            print(f"下载失败>>>{i}")

    @func_timeout.func_set_timeout(IMG_DOWNLOAD_TIME_OUT)
    def _download_img(self, img_name):
        img_real_url = self.reget_img(img_name[0])
        download_item(img_real_url, f"{self.dirpath}/{img_name[1]}{os.path.splitext(img_real_url)[1]}")

    @staticmethod
    def reget_img(img_url):
        return img_url

    def download_img(self, img_name):
        success = True
        for count in range(self.IMG_DOWNLOAD_MAX_FAILED):
            try:
                self._download_img(img_name)
                self.success_count += 1
                success = True
                break
            except Exception:
                success = False
        if not success:
            self.failed_count += 1
            self.failed_urls.append(img_name[0])

