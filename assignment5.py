import jieba
import re
import logging


def cut_word(string):
    l = jieba.lcut(string)
    return l


def tokenize(string):
    # 正则表达式选择 中文和数字部分, 原本有5.3亿字符，去掉英文子母后剩下3.7亿
    p = re.compile(r'<.*?>')
    return ''.join(re.findall('[\u4e00-\u9fa5|\d]+', p.sub('',string)))

def write_token_to_f(open_file, output_file):
    words = []
    for line in open(open_file):
            w = list(jieba.cut(line))
            words += w + ['\n']
            ## 繁体字转换成简体字
    output_file.writelines(' '.join(words))



with open("wikicorpus_training.txt",'w',encoding='utf-8') as outputfile:
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    name_file = "zh_wiki_00"
    write_token_to_f(name_file,outputfile)
    print("done")

