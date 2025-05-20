import pathlib
from PIL import Image
import torch
import numpy as np
import os
import re

class LoadImageWithFilename:
    @classmethod
    def INPUT_TYPES(cls):
        # Alle Dateien im ComfyUI input-Ordner listen
        import folder_paths
        input_dir = folder_paths.get_input_directory()
        files = [f.name for f in pathlib.Path(input_dir).iterdir() if f.is_file()]
        return {
            "required": {
                "image": (sorted(files), {"image_upload": True}),
                "trim_marker": ("STRING", {"default": ""}),
            }
        }

    CATEGORY = "CustomNodes/Simple"
    RETURN_TYPES = ("IMAGE", "STRING", "STRING")
    RETURN_NAMES = ("image", "image_path", "filename")
    FUNCTION = "load_image"

    def load_image(self, image, trim_marker=""):
        import folder_paths
        # Hole den vollständigen Pfad zur gewählten Datei
        image_path = folder_paths.get_annotated_filepath(image)
        filename = os.path.basename(image_path)
        name, _ = os.path.splitext(filename)
        name = re.sub(r"\s\(\d+\)$", "", name)
        
        # Trim Marker anwenden, falls vorhanden
        if trim_marker and trim_marker in name:
            name = name.split(trim_marker, 1)[0]
        
        # Lade das Bild mit PIL
        img = Image.open(image_path).convert("RGB")
        # Bild als Float-Tensor (Batch, Height, Width, Channels)
        np_img = np.array(img).astype(np.float32) / 255.0
        tensor_img = torch.from_numpy(np_img)[None,]  # Batch-Dimension hinzufügen
        return (tensor_img, image_path, name)

# ComfyUI Node-Mapping
NODE_CLASS_MAPPINGS = {
    "LoadImageWithFilename": LoadImageWithFilename
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImageWithFilename": "Load Image, Path and Filename"
}
