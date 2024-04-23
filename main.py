import numpy as np
from tqdm import tqdm
import argparse
from pathlib import Path
from pycocotools.coco import COCO

from utils import xyxy2xywhn
import config

def coco2yolo(names, coco):
    """
    Convert COCO to YOLO
    Args:
        names: str
        coco: str
    """
    
    for cid, category in enumerate(names):
        catIds = coco.getCatIds(catNms=[category])
        imgIds = coco.getImgIds(catIds=catIds)
        for im in tqdm(coco.loadImgs(imgIds), desc=f'Class {cid + 1}/{len(names)} {category}'):
            width, height = im["width"], im["height"]
            img_filename = Path(im["file_name"])                        
                      
            with open(config.YOLO_LABEL_PATH + img_filename.with_suffix('.txt').name, 'a') as file: 
                annIds = coco.getAnnIds(imgIds=im["id"], catIds=catIds, iscrowd=None)
                for bbox in coco.loadAnns(annIds):
                    x, y, w, h = bbox['bbox']  
                    xyxy = np.array([x, y, x + w, y + h])[None]  # pixels(1,4)
                    x, y, w, h = xyxy2xywhn(xyxy, w=width, h=height, clip=True)[0]  # normalized and clipped
                    file.write(f"{cid} {x:.5f} {y:.5f} {w:.5f} {h:.5f}\n")
           
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--coco2yolo", action="store_true", help="COCO to YOLO")   
    
    args = parser.parse_args()

    if args.coco2yolo:
        print("COCO to YOLO")       

        coco = COCO(config.JSON_PATH)
        names = [x["name"] for x in coco.loadCats(coco.getCatIds())]    
        coco2yolo(names, coco)   

        
