#!/usr/bin/python3
""" You can assume all keys will be positive integers """


def canUnlockAll(boxes):
    """ You can assume all keys will be positive integers """
    seen_boxes = {0}
    unseen_boxes = set(boxes[0])

    while unseen_boxes:
        box_idx = unseen_boxes.pop()
        if 0 <= box_idx < len(boxes) and box_idx not in seen_boxes:
            unseen_boxes.update(boxes[box_idx])
            seen_boxes.add(box_idx)

    return len(boxes) == len(seen_boxes)
