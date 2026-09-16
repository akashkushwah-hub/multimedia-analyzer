import os
from pymediainfo import MediaInfo
from file_utils import FileUtils

class VideoAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def analyze(self) -> dict:
        media_info = MediaInfo.parse(self.file_path)
        
        report_data = {
            "general": {
                "file_name": os.path.basename(self.file_path),
                "file_size": FileUtils.get_file_size(self.file_path),
                "container": "N/A",
                "duration": "N/A"
            },
            "video": {
                "resolution": "N/A",
                "frame_rate": "N/A",
                "bit_rate": "N/A",
                "codec": "N/A"
            },
            "audio": {
                "codec": "N/A",
                "channels": "N/A",
                "sampling_rate": "N/A",
                "bit_rate": "N/A"
            },
            "metadata": {}
        }

        for track in media_info.tracks:
            if track.track_type == "General":
                report_data["general"]["container"] = track.format or "N/A"
                if track.duration:
                    duration_sec = float(track.duration) / 1000
                    report_data["general"]["duration"] = f"{duration_sec:.2f} s"
                report_data["metadata"]["Title"] = track.title or "N/A"
                report_data["metadata"]["Writing Application"] = track.writing_application or "N/A"

            elif track.track_type == "Video":
                if track.width and track.height:
                    report_data["video"]["resolution"] = f"{track.width}x{track.height}"
                report_data["video"]["frame_rate"] = f"{track.frame_rate} fps" if track.frame_rate else "N/A"
                report_data["video"]["bit_rate"] = f"{track.bit_rate} bps" if track.bit_rate else "N/A"
                report_data["video"]["codec"] = track.codec_id or track.format or "N/A"

            elif track.track_type == "Audio":
                report_data["audio"]["codec"] = track.codec_id or track.format or "N/A"
                report_data["audio"]["channels"] = str(track.channel_s) if track.channel_s else "N/A"
                report_data["audio"]["sampling_rate"] = f"{track.sampling_rate} Hz" if track.sampling_rate else "N/A"
                report_data["audio"]["bit_rate"] = f"{track.bit_rate} bps" if track.bit_rate else "N/A"

        return report_data

    def print_report(self) -> None:
        data = self.analyze()
        gen = data["general"]
        vid = data["video"]
        aud = data["audio"]
        meta = data["metadata"]

        report = f"""================================
 VIDEO METADATA REPORT
 ================================
 
 File Name       : {gen['file_name']}
 File Size       : {gen['file_size']}
 Container       : {gen['container']}
 Duration        : {gen['duration']}
 
 VIDEO
 --------------------------------
 Resolution      : {vid['resolution']}
 Frame Rate      : {vid['frame_rate']}
 Bit Rate        : {vid['bit_rate']}
 Codec           : {vid['codec']}
 
 AUDIO
 --------------------------------
 Codec           : {aud['codec']}
 Channels        : {aud['channels']}
 Sampling Rate   : {aud['sampling_rate']}
 Bit Rate        : {aud['bit_rate']}
 
 METADATA
 --------------------------------"""
        for k, v in meta.items():
            report += f"\n {k:<15} : {v}"

        print(report)