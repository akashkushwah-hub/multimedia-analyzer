import os
import mimetypes

class FileUtils:
    @staticmethod
    def exists(file_path: str) -> bool:
        return os.path.isfile(file_path)

    @staticmethod
    def get_file_size(file_path: str) -> str:
        size_bytes = os.path.getsize(file_path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"

    @staticmethod
    def get_extension(file_path: str) -> str:
        return os.path.splitext(file_path)[1].lower()

    @staticmethod
    def identify_file_type(file_path: str) -> str:
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type:
            if mime_type.startswith('image/'):
                return 'IMAGE'
            elif mime_type.startswith('audio/'):
                return 'AUDIO'
            elif mime_type.startswith('video/'):
                return 'VIDEO'
        
        # Fallback by extension
        ext = FileUtils.get_extension(file_path)
        if ext in ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']:
            return 'IMAGE'
        elif ext in ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a']:
            return 'AUDIO'
        elif ext in ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv']:
            return 'VIDEO'
            
        return 'UNKNOWN'