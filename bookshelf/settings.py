# Scrapy settings for bookshelf project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable

BOT_NAME = 'bookshelf'

SPIDER_MODULES = [
                  'bookshelf.spiders.source',
                  'bookshelf.spiders.home',
                  'bookshelf.spiders.search'
                  ]
NEWSPIDER_MODULE = 'bookshelf.spiders'
ITEM_PIPELINES = {
    'bookshelf.pipelines.BookPipeline' : 500,
    'bookshelf.pipelines.BookDescPipeline' : 501,
    'bookshelf.pipelines.SectionsPipeline' : 502,
    'bookshelf.pipelines.DropPipeline' : 503
}
DOWNLOAD_TIMEOUT = 30
CONCURRENT_REQUESTS = 128

DUPEFILTER_DEBUG = True
DUPEFILTER_CLASS = 'bookshelf.dupefilters.UnFilterDupeFilter'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.79 Safari/535.11'
DEFAULT_REQUEST_HEADERS = {
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'gzip,deflate,sdch',
                           'Accept-Language': 'zh-CN,zh;q=0.8',
                           'Connection': 'keep-alive'
                           }


# LOG_FILE = 'bookshelf.log'
# LOG_LEVEL = 'DEBUG'

MEMDEBUG_NOTIFY = ['zhiying8710@hotmail.com']
ROBOTSTXT_OBEY = False

every_crawl_timedelta_mins = 3
source_spider_sleep_secs = 60 * 10

# config
ingrone_spiders = set(['qdhome', 'zhhome', 'cshome'])
source_home_spiders = {
                       'qd' : 'qdhome',
                       'zh' : 'zhhome',
                       'cs' : 'cshome'
                       }
spider_redis_queues = {
                       'qdhome' : '__qidian_home_queue',
                       'zhhome' : '__zongheng_home_queue',
                       'cshome' : '__chuangshi_home_queue'
                       }
search_spider_queues = {
                        'qdhome' : '__qd_sea_queue',
                        'zhhome' : '__zh_sea_queue'
                        }
unupdate_retry_queue = '__unupdate_retry_queue'
crawling_key_prefix = '__crawling_'
crawling_key_expire = 3 * 60  # this must less than source_spider_sleep
last_crawl_time_key = '__last_crawl_time'

user_favos_update_counts_key_prefix = '__user_favos_update_counts_'

mongo_host = '127.0.0.1'
mongo_port = 27017
redis_host = '127.0.0.1'
redis_port = 6379
redis_def_db = 0
redis_sep = ':::'


