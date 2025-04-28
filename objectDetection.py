import os
import tensorflow as tf
from pixellib.instance import instance_segmentation

default_model_path = "./mask_rcnn_coco.h5"

def setup_eager_execution():
    try:
        tf.compat.v1.enable_eager_execution()
    except Exception:
        pass

def load_segmentation_model(model_path):
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    segmenter = instance_segmentation()
    segmenter.load_model(model_path)
    return segmenter

def segment_image(segmenter, args, target_classes):
    if not os.path.isfile(args.input):
        raise FileNotFoundError(f"Input image not found: {args.input}")

    common_kwargs = dict(
        image_path=args.input,
        segment_target_classes=target_classes,
        show_bboxes=True
    )

    if args.action == 'segment':
        segmenter.segmentImage(
            **common_kwargs,
            output_image_name=args.output
        )
        print(f"Segmented image saved to: {args.output}")

    elif args.action == 'count':
        result = segmenter.segmentImage(
            **common_kwargs,
            output_image_name=args.output
        )
        counts = {}
        for cls in result["class_ids"]:
            counts[cls] = counts.get(cls, 0) + 1
        print("Object count by class ID: ", counts)

    elif args.action == 'extract':
        segmenter.segmentImage(
            **common_kwargs,
            extract_segmented_objects=True,
            save_extracted_objects=True
        )
        print("Extracted objects saved as individual files.")
        
    elif args.action == 'mask':
        segmenter.segmentImage(
            **common_kwargs,
            output_image_name=args.output,
            show_mask=True
        )
        print(f"Masked output saved to: {args.output}")
    
    else:
        raise ValueError(f"Unknown action: {args.action}")

def segment_video(segmenter, args, target_classes):
    if not os.path.isfile(args.input):
        raise FileNotFoundError(f"Input video not found: {args.input}")

    common_kwargs = dict(
        video_path=args.input,
        segment_target_classes=target_classes,
        show_bboxes=True
    )

    if args.action == 'segment':
        segmenter.segmentVideo(
            **common_kwargs,
            output_image_name=args.output
        )
        print(f"Segmented video saved to: {args.output}")

    elif args.action == 'count':
        result = segmenter.segmentVideo(
            **common_kwargs,
            output_image_name=args.output
        )
        counts = {}
        for cls in result["class_ids"]:
            coiunts[cls] = counts.get(cls, 0) + 1
        print("Object count by class ID: ", counts)

    elif args.action == 'extract':
        segmenter.segmentVideo(
            **common_kwargs,
            extract_segmented_objects=True,
            save_extracted_objects=True
        )
        print("Extracted objects saved as individual video clips.")
        
    elif args.action == 'mask':
        segmenter.segmentVideo(
            **common_kwargs,
            output_image_name=args.output,
            show_mask=True
        )
        print(f"Masked video saved to: {args.output}")
    
    else:
        raise ValueError(f"Unknown action: {args.action}")

def get_user_choices():
    user_model = input(f"Enter path to Mask R-CNN model (.h5) [default: {default_model_path}]: ").strip()
    model_path = user_model if user_model else default_model_path

    input_path = input("Enter path to input image or video: ").strip()
    ext = os.path.splitext(input_path)[1].lower()
    if ext in [".jpg", ".jpeg", ".png"]:
        is_video = False
    elif ext in [".mp4", ".avi", ".mov"]:
        is_video = True
    else:
        raise ValueError("Unsupported file extension. Use jpeg/png for images or mp4/avi/mov for videos.")    

    default_out = "output_video.mp4" if is_video else "output.jpg"
    output_path = input(f"Enter output path [default: {default_out}]: ").strip()
    if not output_path:
        output_path = default_out
    
    cls_input = input("Enter target classes separated by commas (e.g. person,car) [default: person]: ").strip()
    classes = [c.strip() for c in cls_input.split(",")] if cls_input else ["person"]


    print("Select action on segmented objects:")
    print("  1) Just segment and save")
    print("  2) Count each class and print totals")
    print("  3) Extract each object to its own file")
    print("  4) Show/save only masks")
    action_map = {"1": "segment", "2": "count", "3": "extract", "4": "mask"}
    choice = input("Enter 1, 2, 3, or 4 [default: 1]: ").strip()
    action = action_map.get(choice, "segment")

    class Args: pass
    args = Args()
    args.model = model_path
    args.input = input_path
    args.output = output_path
    args.classes = classes
    args.action = action
    args.is_video = is_video
    return args

def main():
    setup_eager_execution()
    args = get_user_choices()
    
    segmenter = load_segmentation_model(args.model)
    target_classes = segmenter.select_target_classes(**{cls: True for cls in args.classes})

    if args.is_video:
        segment_video(segmenter, args, target_classes)

    else:
        segment_image(segmenter, args, target_classes)

if __name__ == '__main__':
    main()





    
