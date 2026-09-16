from PIL import Image, ExifTags
import os

class ImageAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def analyze(self) -> dict:
        data = {
            "file_name": os.path.basename(self.file_path),
            "format": "N/A",
            "resolution": "N/A",
            "color_mode": "N/A",
            "exif": {}
        }
        
        try:
            with Image.open(self.file_path) as img:
                data["format"] = img.format
                data["resolution"] = f"{img.width}x{img.height}"
                data["color_mode"] = img.mode

                exif_data = img._getexif()
                if exif_data:
                    for tag, value in exif_data.items():
                        tag_name = ExifTags.TAGS.get(tag, tag)
                        data["exif"][str(tag_name)] = str(value)
        except Exception as e:
            data["error"] = str(e)
            
        return data