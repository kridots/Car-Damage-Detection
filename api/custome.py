import detectron2
from detectron2.utils.logger import setup_logger
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer, ColorMode
from detectron2.data import MetadataCatalog
from detectron2.data import (
    DatasetCatalog,
)  # Optional, if using custom datasets for evaluation
import cv2
import numpy as np

# Define the path to your saved model weights
model_weights_path = "./output/model_final.pth"  # Replace with your actual path


class CarDamageDetector:
    def __init__(self):
        # Load configuration
        cfg = get_cfg()
        cfg.MODEL.DEVICE = "cpu"  # Change to "cuda" if using GPU
        cfg.merge_from_file("./config.yml")
        cfg.DATASETS.TEST = ("car_dataset_val",)
        # Load model weights
        cfg.MODEL.WEIGHTS = model_weights_path

        # Set the testing threshold for predictions (optional, adjust as needed)
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7

        # Create predictor
        self.predictor = DefaultPredictor(cfg)

        # Optionally, load metadata if you have a custom dataset
        self.metadata = MetadataCatalog.get("car_dataset_val")

    def predict(self, image):
        """
        Performs car damage detection on a given image.

        Args:
            image: NumPy array representing the image (BGR format).

        Returns:
            A dictionary containing the predicted detections and the visualized image.
        """

        # Convert image to RGB format (expected by Detectron2)
        image = image[:, :, ::-1]

        # Perform prediction
        outputs = self.predictor(image)
        print("meta", self.metadata)
        # Create visualizer
        v = Visualizer(
            image[:, :, ::-1],
            metadata=self.metadata,
            scale=0.5,
            instance_mode=ColorMode.IMAGE_BW,  # optional, remove unsegmented pixel colors
        )

        # Visualize predictions
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))

        # Convert back to BGR format for potential display
        predicted_image = out.get_image()[:, :, ::-1]

        return {
            "detections": outputs,
            "predicted_image": predicted_image,
        }


if __name__ == "__main__":
    # Load the model
    detector = CarDamageDetector()

    # Load your test image (replace with your image loading logic)
    # image = cv2.imread("F:\Kritesh\car-damage\dataset\img\\4.jpg")
    image = cv2.imread("F:\Kritesh\car-damage\dataset\\val\\3.jpg")
    # image = cv2.imread("dataset/test/60.jpg")

    # Make prediction
    results = detector.predict(image)
    print("RESULT:>", results)
    # Access detections and predicted image
    detections = results["detections"]
    predicted_image = results["predicted_image"]

    # Optional: Process detections or visualize the predicted image
    # ...

    cv2.imshow("Car Damage Detection", predicted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
