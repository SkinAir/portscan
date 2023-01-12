import argparse
from ast import arg
from distutils.log import error
from importlib.resources import contents
from multiprocessing import Lock
from pydoc import cli
import socket  # 创建TCP连接
from threading import Thread
import threading  # 多线程模块，进行多线程扫描
import time
import argparse
from unittest import result  # 时间模块，记录扫描所需时间


def creat_list():#创建全局变量
    global result
    result = []

def read_ip(file):
    with open(file,'r',encoding='utf-8') as f:#读取ip文件
        lines = f.readlines()
    content = [x.strip() for x in lines]
    return content#将ip生成列表

def clear():
    file = open("result.txt", 'w').close()#清空文件内容

def thread_run(target,result):
    port_list = [21,22,23,25,69,80,81,82,83,84,110,135,389,389,443,445,488,512,513,514,873,901,902,903,1000,1001,1043,1050,1080,1099,1090,1158,1352,1433,1434,1521,1658,2049,2100,2181,2601,2604,3128,3306,3307,3389,4440,4444,4445,4848,5000,5280,5357,5432,5500,5632,5900,5901,5902,5903,5984,6000,6033,6082,6379,6666,7001,7001,7002,7070,7101,7676,7777,7899,7988,8000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8069,8080,8081,8082,8083,8084,8085,8086,8087,8088,8089,8090,8091,8092,8093,8094,8095,8098,8099,8980,8990,8443,8686,8787,8880,8888,9000,9001,9043,9045,9060,9080,9081,9088,9088,9090,9091,9100,9200,9300,9443,9871,9999,10000,10068,10086,11211,20000,22022,22222,27017,28017,50060,50070]
    for port in port_list:  # 定义扫描的端口
        # 2、启动多线程运行PortScan函数
        t = Thread(target=portscan, args=(target, port))  # 创建线程对象
        t.start()  # 开始线程

def portscan(target, port):
    # 1、定义portscan函数，进行TCP端口扫描
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象
        try:
            client.connect((target, port))  # 建立TCP连接
            client.shutdown(2)
            result.append(port)
            #lock.acquire()
            # with open('result.txt','a',encoding='utf-8')as f:#写入结果
            #     results = str(result)
            #     results = results+'\n'
            #     f.write("[*] %s 开放端口: %s" % (target,results))
            #     f.close()
            #lock.release()
        except:
            error
        #连接成功则添加进result列表，失败则except
        #print("[*] %s:%d端口开放" % (target, port))

        client.close()
    except:
        pass  # 捕获异常

def write(target):
    with open('result.txt','a',encoding='utf-8')as f:#写入结果
        results = str(result)
        results = results+'\n'
        print("[*] %s 开放端口: %s" % (target,results))
        f.write("[*] %s 开放端口: %s" % (target,results))
        f.close()


lock = threading.Lock()

def parse_args():
    #创建解析对象
    parser = argparse.ArgumentParser()
    #添加命令
    parser.add_argument("-i","--ip",help="Add IP after parameter")
    parser.add_argument("-f","--file",help="Add filename after parameter")
    #解析复制给args
    args = parser.parse_args()
    return args

def main():
    start_time = time.time()
    clear()
    args = parse_args()
    args.ip == str(args.ip)
    if args.ip == None:
        content = read_ip(args.file)
        #content = str(content)
        for target in content:
            creat_list()
            thread_run(target,result)
            write(target)
    else:
        target = str(args.ip)#parse传入
        creat_list()
        thread_run(target,result)
        write(target)
    end_time = time.time()
    print("[*] All done in %.2f s" % (end_time - start_time))#打印结束时间


if __name__ == "__main__":
    main()
