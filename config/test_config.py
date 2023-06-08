class Config:
    model_weights = "./frcnn_model/"
    image_path = "/kaggle/input/crop-dataset-coco-format/ml-project-data-annotated-coco/test"
    gpu_id = '2'
    num_classes = 2 + 1
    data_root_dir = "/kaggle/input/crop-dataset-coco-format/ml-project-data-annotated-coco"


test_cfg = Config()
