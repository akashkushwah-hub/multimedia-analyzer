import json
import os

class ReportGenerator:
    @staticmethod
    def save_json(data: dict, output_path: str = "reports/report.json") -> None:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"\n[+] Consolidated report saved to: {output_path}")