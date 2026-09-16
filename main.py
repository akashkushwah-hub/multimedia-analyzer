import sys
from file_utils import FileUtils
from image_analyzer import ImageAnalyzer
from audio_analyzer import AudioAnalyzer
from video_analyzer import VideoAnalyzer
from report_generator import ReportGenerator

def process_file(file_path: str) -> dict:
    if not FileUtils.exists(file_path):
        print(f"Error: File not found -> {file_path}")
        return {}

    file_type = FileUtils.identify_file_type(file_path)
    print(f"\nDetected File Type: {file_type} for path: {file_path}")

    if file_type == 'IMAGE':
        analyzer = ImageAnalyzer(file_path)
        return {"type": "IMAGE", "data": analyzer.analyze()}
    elif file_type == 'AUDIO':
        analyzer = AudioAnalyzer(file_path)
        return {"type": "AUDIO", "data": analyzer.analyze()}
    elif file_type == 'VIDEO':
        analyzer = VideoAnalyzer(file_path)
        analyzer.print_report()  # Prints standard report format from Lab 3
        return {"type": "VIDEO", "data": analyzer.analyze()}
    else:
        print("Error: Unsupported file format.")
        return {}

def main():
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
        result = process_file(target_path)
        if result:
            ReportGenerator.save_json(result)
    else:
        # Default run over available samples
        sample_files = [
            "samples/image.jpg",
            "samples/song.mp3",
            "samples/video.mp4"
        ]
        
        consolidated_results = []
        for sample in sample_files:
            if FileUtils.exists(sample):
                res = process_file(sample)
                if res:
                    consolidated_results.append(res)
            else:
                print(f"Sample file {sample} not found. Skipping...")

        if consolidated_results:
            ReportGenerator.save_json(consolidated_results)

if __name__ == "__main__":
    main()