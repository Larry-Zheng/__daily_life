import os
import json
import numpy as np
import cv2


model = r'''
<annotation>
	<folder>{folder}</folder>
	<filename>{filename}</filename>
	<path>{path}</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>{w}</width>
		<height>{h}</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>{obj}
</annotation>

'''
picFormat = 'jpg'
mainPath = os.getcwd()

def genObj(n,xmi,xma,ymi,yma):
    '''生成obj节点'''
    res = r'''
    <object>
		<name>{name}</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>{xmin}</xmin>
			<ymin>{ymin}</ymin>
			<xmax>{xmax}</xmax>
			<ymax>{ymax}</ymax>
		</bndbox>
	</object>'''
    return res.format(name = n, xmin = xmi, ymin = ymi , xmax = xma ,ymax = yma )


if __name__ == '__main__':

    obj = [ f for f in os.listdir() if '.json' in f]
    for js in obj:
        with open(js,'r') as f:
            content = json.load(f)['shapes']

        names = [c['label'] for c in content]  #类别s
        pointSets = [np.array(c['points']) for c in content]  #点集s
        img  = cv2.imread('../photo/'+js.replace('json',picFormat),0)
        h,w = img.shape  #图像长宽
        obj = ''  #图像节点

        for name,points in zip(names,pointSets):
            xmin,xmax = points[:,0].min(),points[:,0].max()
            ymin,ymax = points[:,1].min(),points[:,1].max()
            xmin,xmax,ymin,ymax = int(xmin),int(xmax),int(ymin),int(ymax)
            obj += genObj(name,xmin,xmax,ymin,ymax)

        xmlContent = model.format(
                                #   folder = mainPath.split('\\')[-1],
                                  folder = 'xxx',
                                  filename = js.replace('json',picFormat),
                                #   path = mainPath+r'\%s'%js.replace('json',picFormat),
                                  path = 'xxx',
                                  w = w,
                                  h = h,
                                  obj = obj
                                  )
        with open(js.replace('json','xml'),'w') as f:
            f.write(xmlContent)

