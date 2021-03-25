"""
DESCRIPTION:
------------
Write_brief_summary_of_what_the_function_will_do

PARAMETERS:
-----------
Parameter_1: Description_with_example_if_needed
Parameter_2: Description_with_example_if_needed

RETURNS:
--------
DataType: Describe_what_is_being_returned

"""

# Here are a few examples of how to use it

def get_model_scores(pred_boxes):
    """
    DESCRIPTION:
    ------------
    Creates a dictionary from model_scores to image ids

    PARAMETERS:
    -----------
    pred_boxes (dict): dict of dicts of 'boxes' and 'scores'

    RETURNS:
    --------
    dict: keys are model_scores and values are image ids (usually filenames)

    """
    model_score = {}
    for img_id, val in pred_boxes.items():
        for score in val['scores']:
            if score not in model_score.keys():
                model_score[score] = [img_id]
            else:
                model_score[score].append(img_id)
    return model_score
  
  
 def calc_iou(gt_bbox, pred_bbox):
    """
    DESCRIPTION:
    ------------
    Calculates predicted and ground truth bounding boxes to return 
    the Intersection Over Union (IoU) ratio.

    PARAMETERS:
    -----------
    gt_bbox (dict): dict that lists ground truth (gt) bounding boxes
    pred_bbox (dict): dict of dicts of 'boxes' and 'scores'

    RETURNS:
    --------
    Float: Intersection Over Union (IoU) Ratio

    """
    x_topleft_gt, y_topleft_gt, x_bottomright_gt, y_bottomright_gt = gt_bbox
    x_topleft_p, y_topleft_p, x_bottomright_p, y_bottomright_p = pred_bbox

    if (x_topleft_gt > x_bottomright_gt) or (y_topleft_gt > y_bottomright_gt):
        raise AssertionError("Ground Truth Bounding Box is not correct")
    if (x_topleft_p > x_bottomright_p) or (y_topleft_p > y_bottomright_p):
        raise AssertionError("Predicted Bounding Box is not correct",
                             x_topleft_p, x_bottomright_p, y_topleft_p,
                             y_bottomright_gt)

    # if the GT bbox and predcited BBox do not overlap then iou=0
    if (x_bottomright_gt < x_topleft_p):
        # If bottom right of x-coordinate  GT  bbox is less than or above the top left of x coordinate of  the predicted BBox

        return 0.0
    if (
            y_bottomright_gt < y_topleft_p
    ):  # If bottom right of y-coordinate  GT  bbox is less than or above the top left of y coordinate of  the predicted BBox

        return 0.0
    if (
            x_topleft_gt > x_bottomright_p
    ):  # If bottom right of x-coordinate  GT  bbox is greater than or below the bottom right  of x coordinate of  the predcited BBox

        return 0.0
    if (
            y_topleft_gt > y_bottomright_p
    ):  # If bottom right of y-coordinate  GT  bbox is greater than or below the bottom right  of y coordinate of  the predcited BBox

        return 0.0

    GT_bbox_area = (x_bottomright_gt - x_topleft_gt + 1) * (y_bottomright_gt -
                                                            y_topleft_gt + 1)
    Pred_bbox_area = (x_bottomright_p - x_topleft_p + 1) * (y_bottomright_p -
                                                            y_topleft_p + 1)

    x_top_left = np.max([x_topleft_gt, x_topleft_p])
    y_top_left = np.max([y_topleft_gt, y_topleft_p])
    x_bottom_right = np.min([x_bottomright_gt, x_bottomright_p])
    y_bottom_right = np.min([y_bottomright_gt, y_bottomright_p])

    intersection_area = (x_bottom_right - x_top_left + 1) * (y_bottom_right -
                                                             y_top_left + 1)

    union_area = (GT_bbox_area + Pred_bbox_area - intersection_area)

    return intersection_area / union_area
