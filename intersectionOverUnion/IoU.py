import torch

def intersectionOverUnion(boxes_preds, boxes_labels,box_format="midpoint"):
    """
    """
    if box_format=="coners":
        box1_x1=boxes_preds[...,0:1]
        box1_y1=boxes_preds[...,1:2]
        box1_x2=boxes_preds[...,2:3]
        box1_y2=boxes_preds[...,3:4]
        box2_x1=boxes_preds[...,0:1]
        box2_y1=boxes_preds[...,1:2]
        box2_x2=boxes_preds[...,2:3]
        box2_y2=boxes_preds[...,3:4]
    if box_format=="midpoints":
        box1_x1=boxes_preds[...,0:1]
        box1_y1=boxes_preds[...,1:2]
        box1_x2=boxes_preds[...,2:3]
        box1_y2=boxes_preds[...,3:4]
        box2_x1=boxes_labels[...,0:1]
        box2_y1=boxes_labels[...,1:2]
        box2_x2=boxes_labels[...,2:3]
        box2_y2=boxes_labels[...,3:4]
            
    x1= torch.max(box1_x1,box2_x1)
    y1= torch.max(box1_y1,box2_y1)
    x2= torch.max(box1_x2,box2_x2)
    y2= torch.max(box1_y2,box2_y2)

    intersection = (x1-x2).clamp(0)*(y1-y2).clamp(0) #when they do not intersection
    box1_area=abs((box1_x1-box1_x2)*(box1_y1-box1_y2))
    box2_area=abs((box2_x1-box2_x2)*(box2_y1-box2_y2))

    return intersection/(box1_area+box2_area-intersection)#since intersection added twice here while getting the union