
import pandas as pd
from utils.roadmap import generate_roadmap

def save_roadmap_to_csv(output_path="reports/90_day_roadmap.csv"):
    roadmap = generate_roadmap()
    df = pd.DataFrame(roadmap)
    df.to_csv(output_path, index=False)
    print(f"✅ 90-day roadmap saved to {output_path}")

if __name__ == "__main__":
    save_roadmap_to_csv()
