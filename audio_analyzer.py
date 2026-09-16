from tinytag import TinyTag
import os

class AudioAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def analyze(self) -> dict:
        data = {
            "file_name": os.path.basename(self.file_path),
            "codec": "N/A",
            "duration": "N/A",
            "bitrate": "N/A",
            "samplerate": "N/A",
            "channels": "N/A",
            "tags": {}
        }

        try:
            tag = TinyTag.get(self.file_path)
            data["codec"] = os.path.splitext(self.file_path)[1].upper().replace('.', '')
            data["duration"] = f"{tag.duration:.2f} s" if tag.duration else "N/A"
            data["bitrate"] = f"{tag.bitrate} kbps" if tag.bitrate else "N/A"
            data["samplerate"] = f"{tag.samplerate} Hz" if tag.samplerate else "N/A"
            data["channels"] = str(tag.channels) if tag.channels else "N/A"
            
            data["tags"] = {
                "Title": tag.title or "N/A",
                "Artist": tag.artist or "N/A",
                "Album": tag.album or "N/A"
            }
        except Exception as e:
            data["error"] = str(e)

        return data