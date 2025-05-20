
import os

class ExtractAndTrimFilename:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {"default": "C:/Images/Image_xyz_123.png"}),
                "trim_marker": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("processed_filename",)
    FUNCTION = "extract_and_trim"
    CATEGORY = "Utils"

    def extract_and_trim(self, file_path, trim_marker):
        filename = os.path.basename(file_path)
        name, _ = os.path.splitext(filename)
        if trim_marker:
            index = name.find(trim_marker)
            if index != -1:
                name = name[:index]
        return (name,)

NODE_CLASS_MAPPINGS = {
    "ExtractAndTrimFilename": ExtractAndTrimFilename
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExtractAndTrimFilename": "Extract & Trim Filename (No Extension)"
}
