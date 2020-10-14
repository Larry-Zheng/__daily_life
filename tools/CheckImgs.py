import os 
import shutil
from tqdm import tqdm
import cv2
IMG_TYPES = ['jpg','JPG','bmp','BMP','png','PNG','tif','TIF']

class ImgAdviser:
    def __init__(self,db_path,img_ext):
        self.db_path = db_path
        self.img_ext = img_ext
        self._is_img_file = lambda x: any(x.endswith(ext) for ext in IMG_TYPES)
        
        #构造删除区 新img区 新xml区
        self.dump_path = '%s/__dump__'%db_path
        self.new_img_path = '%s/new_img'%db_path
        self.new_xml_path = '%s/new_xml'%db_path
        self._rmdir(self.dump_path)
        self._rmdir(self.new_img_path)
        self._rmdir(self.new_xml_path)
        self._mkdir(self.dump_path)
        self._mkdir(self.new_img_path)
        self._mkdir(self.new_xml_path)

        #规整图片后缀
        self._InitImgExt()

        #剔除

        #获取图片路径和xml路径 & 名字
        print('scanning img...')
        self.img_pathes,self.img_names = self._ScanImgFiles()  #检测图片是否可读
        print('scanning xml...')
        self.xml_pathes,self.xml_names = self._ScanXmlFiles()


        #img中多的 剔除
        print('pairing img...')
        self._ImgPairXml()

        #xml剔除多余的
        print('pairing xml...')
        self._XmlPairImg()



    def _mkdir(self,dirpath):
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
    
    def _rmdir(self,dirpath):
        if os.path.exists(dirpath):
            shutil.rmtree(dirpath)

    def _InitImgExt(self):
        for head,_,files in os.walk(self.db_path):
            head = head.replace('\\','/')
            for file in files:
                im_path = '%s/%s'%(head,file)
                if self._is_img_file(im_path):
                    _, ext = os.path.splitext(im_path)
                    os.rename(im_path,im_path.replace(ext,self.img_ext))
    
    def _ScanImgFiles(self):
        img_path_collectors = []
        img_name_collector = []
        for head,_,files in os.walk(self.db_path):
            head = head.replace('\\','/')
            for file in tqdm(files):
                im_path = '%s/%s'%(head,file)
                if im_path.endswith(self.img_ext) and '__dump__' not in im_path :
                    try:
                        cv2.imread(im_path).astype('float32')
                    except Exception as e:
                        print(im_path,' dumped:',e)
                        shutil.copy(im_path,self.dump_path)
                        continue

                    img_path_collectors.append(im_path)
                    img_name_collector.append(file.strip(self.img_ext))
        
        return img_path_collectors,img_name_collector
    

    def _ScanXmlFiles(self):
        xml_path_collectors = []
        xml_name_collectors = []
        for head,_,files in os.walk(self.db_path):
            head = head.replace('\\','/')
            for file in tqdm(files):
                xml_path = '%s/%s'%(head,file)
                if xml_path.endswith('.xml') and '__dump__' not in xml_path:
                    xml_path_collectors.append(xml_path)
                    xml_name_collectors.append(file.strip('.xml'))
        return xml_path_collectors,xml_name_collectors
    
    def _ImgPairXml(self):
        for i,im_name in enumerate(tqdm(self.img_names)):
            if im_name in self.xml_names:
                shutil.copy(self.img_pathes[i],self.new_img_path)
            else:
                shutil.copy(self.img_pathes[i],self.dump_path)
            
    
    def _XmlPairImg(self):
        for i,xml_name in enumerate(tqdm(self.xml_names)):
            if xml_name in self.img_names:
                shutil.copy(self.xml_pathes[i],self.new_xml_path)
            else:
                shutil.copy(self.xml_pathes[i],self.dump_path)
        

    

if __name__ == '__main__':
    Ad = ImgAdviser('5Kxy','.jpg')