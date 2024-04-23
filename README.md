### Conversion tool:  COCO to YOLO 

### Usage

```
git clone https://github.com/jabborov/coco2yolo.git
cd coco2yolo
pip install -r requirements.txt
```

Edit variables in `config.py`  to align with your custom dataset.

**Convert COCO to YOLO**
```
python main.py --coco2yolo
```

`<object-class> <x_center> <y_center> <width> <height>`

**where:**
- `<object-class>` - integer object number from `0` to `(classes amount -1)`
- `<x_center> <y_center> <width> <height>` - `float` values relative to width and height of image, the range equals to `(0.0 to 1.0]`
- For example: `<x> = <absolute_x> / <image_width>` or `<height> = <absolute_height> / <image_height>`
- Attention: `<x_center> <y_center>` - are center of rectangle (are not top-left corner)

**Convert YOLO to VOC**     
[Click here](https://github.com/jabborov/yolo2voc.git)

### References
1. https://github.com/ultralytics/yolov5/blob/master/utils/general.py
2. https://github.com/AlexeyAB/darknet
