import requests
import random
import time
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"

sensors = {
    "traffic_sensors": ["Zone_A", "Zone_B", "Zone_C", "Zone_D"],
    "energy_meters": ["District_1", "District_2", "District_3"],
    "waste_bins": ["Bin_01", "Bin_02", "Bin_03", "Bin_04", "Bin_05"],
    "safety_cameras": ["Cam_01", "Cam_02", "Cam_03"]
}

def simulate_traffic():
    return {
        "sensor_type": "traffic",
        "zone": random.choice(sensors["traffic_sensors"]),
        "vehicle_count": random.randint(10, 200),
        "congestion_level": random.choice(["low", "medium", "high"]),
        "timestamp": str(datetime.now())
    }

def simulate_energy():
    return {
        "sensor_type": "energy",
        "meter_id": random.choice(sensors["energy_meters"]),
        "consumption_kw": round(random.uniform(50, 500), 2),
        "solar_output_kw": round(random.uniform(10, 100), 2),
        "timestamp": str(datetime.now())
    }

def simulate_waste():
    level = random.randint(0, 100)
    return {
        "sensor_type": "waste",
        "bin_id": random.choice(sensors["waste_bins"]),
        "fill_level": level,
        "status": "FULL" if level > 80 else "OK",
        "timestamp": str(datetime.now())
    }

def simulate_safety():
    return {
        "sensor_type": "safety",
        "camera_id": random.choice(sensors["safety_cameras"]),
        "motion_detected": random.choice([True, False]),
        "alert_level": random.choice(["normal", "warning", "critical"]),
        "timestamp": str(datetime.now())
    }

print("IoT Simulator Started...")
print("Sending sensor data every 5 seconds\n")

while True:
    traffic = simulate_traffic()
    energy = simulate_energy()
    waste = simulate_waste()
    safety = simulate_safety()

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Sensors fired:")
    print(f"  Traffic  → {traffic['zone']} | vehicles: {traffic['vehicle_count']} | {traffic['congestion_level']}")
    print(f"  Energy   → {energy['meter_id']} | {energy['consumption_kw']} kW")
    print(f"  Waste    → {waste['bin_id']} | {waste['fill_level']}% {'⚠ FULL' if waste['status'] == 'FULL' else ''}")
    print(f"  Safety   → {safety['camera_id']} | alert: {safety['alert_level']}")
    print()

    time.sleep(5)