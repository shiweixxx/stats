#coding:utf-8
import os
from django.conf import settings
from pyexcel_xls import get_data,save_data
from collections import OrderedDict
#from statistics.models import TianRong,QingNiu,GuDe
from models import TianRong,QingNiu,GuDe

class DataSource(object):
    
    def __init__(self,file_list):
        #self.dir_path = os.listdir(dir_path)
        self.filename_list = file_list
        self.tianrong_rs = []
        self.qingniu_rs = []
        self.gude_rs = []
        self.load_data()

    def get_expt_phone_map(self):
        f=open('../conf/phone.txt','r')
        lines=f.readlines()
        f.close()
        #mulsub=lambda x,i,j,s:x[:i] + ''.join(map( lambda it:it.replace(it,s),x[i:j] )) + x[j:]
        return { it.strip('\n'):1 for it in lines} 


    def get_xlx_data(self,fpath):
        return get_data(fpath)

    def load_data(self):
        #for it in self.dir_path:
        for it in self.filename_list:
            if u'青牛' in it:
                print '>>>>>>>>',it
                #self.get_qingniu(settings.UPLOAD_PATH+'/'+it)
                self.get_qingniu(it)
            elif u'古德' in it:
                print 'zzzzzzzzzz',it
                #self.get_gude(settings.UPLOAD_PATH+'/'+it)
                self.get_gude(it)
            elif u'天润' in it:
                print 'xxxxxxxxxxx',it
                #self.get_tianrong(settings.UPLOAD_PATH+'/'+it)
                self.get_tianrong(it)
    def get_tianrong(self,fpath):
        data=get_data(fpath)
        expt_mp=self.get_expt_phone_map()
        rs = data and data['Sheet1'] or []
        for it in rs[1:]:
            if not it[8] or it[9] in expt_mp:
                continue
            tr=TianRong(it)
            self.tianrong_rs.append(tr)
        return self.tianrong_rs

    def get_qingniu(self,fpath):
        data=get_data(fpath)
        rs = data and data['Sheet1'] or []
        for it in rs[4:]:
            tr=QingNiu(it)
            self.qingniu_rs.append(tr)
        return self.qingniu_rs

    def get_gude(self,fpath):
        data=get_data(fpath)
        rs = data and data['Sheet1'] or []
        for it in rs[1:]:
            tr=GuDe(it)
            self.gude_rs.append(tr)
        return self.gude_rs






if __name__=='__main__':
    dt=DataSource('/home/sw/stats/upload')
    
