import sys
import requests
from qdrant_client import QdrantClient, models
from openai import OpenAI
import os
from dotenv import load_dotenv
import psycopg

products = [
    {"id": 1, "name": "iPhone 16", "price": 85000, "description": "Apple smartphone with advanced camera and A18 chip", "stock": 12},
    {"id": 2, "name": "Samsung Galaxy S25", "price": 92000, "description": "Android smartphone with AMOLED display", "stock": 8},
    {"id": 3, "name": "MacBook Air M3", "price": 125000, "description": "Lightweight laptop with Apple M3 chip", "stock": 5},
    {"id": 4, "name": "ASUS ROG Strix", "price": 145000, "description": "Gaming laptop with powerful GPU", "stock": 4},
    {"id": 5, "name": "Dell XPS 15", "price": 130000, "description": "Professional laptop for developers", "stock": 7},
    {"id": 6, "name": "iPad Pro", "price": 110000, "description": "Professional tablet with M4 chip", "stock": 9},
    {"id": 7, "name": "Samsung Tab S9", "price": 65000, "description": "Android tablet with AMOLED screen", "stock": 11},
    {"id": 8, "name": "AirPods Pro 2", "price": 18000, "description": "Wireless earbuds with active noise cancellation", "stock": 20},
    {"id": 9, "name": "Sony WH-1000XM5", "price": 25000, "description": "Premium wireless noise cancelling headphones", "stock": 6},
    {"id": 10, "name": "JBL Flip 6", "price": 9000, "description": "Portable waterproof Bluetooth speaker", "stock": 15},

    {"id": 11, "name": "Logitech G Pro X", "price": 12000, "description": "Professional gaming headset", "stock": 10},
    {"id": 12, "name": "Razer DeathAdder V3", "price": 7500, "description": "High precision gaming mouse", "stock": 14},
    {"id": 13, "name": "Logitech G502", "price": 8500, "description": "Customizable gaming mouse", "stock": 18},
    {"id": 14, "name": "Keychron K8", "price": 11000, "description": "Mechanical wireless keyboard", "stock": 7},
    {"id": 15, "name": "SteelSeries Apex Pro", "price": 22000, "description": "Advanced mechanical gaming keyboard", "stock": 5},
    {"id": 16, "name": "LG UltraGear 27", "price": 35000, "description": "27 inch gaming monitor with high refresh rate", "stock": 8},
    {"id": 17, "name": "Samsung Odyssey G7", "price": 48000, "description": "Curved gaming monitor", "stock": 4},
    {"id": 18, "name": "PlayStation 5", "price": 55000, "description": "Sony next generation gaming console", "stock": 10},
    {"id": 19, "name": "Xbox Series X", "price": 52000, "description": "Microsoft gaming console", "stock": 6},
    {"id": 20, "name": "Nintendo Switch OLED", "price": 30000, "description": "Portable hybrid gaming console", "stock": 9},

    {"id": 21, "name": "Canon EOS R50", "price": 75000, "description": "Mirrorless camera for photography and video", "stock": 3},
    {"id": 22, "name": "Sony Alpha A6400", "price": 85000, "description": "Mirrorless camera with fast autofocus", "stock": 5},
    {"id": 23, "name": "GoPro Hero 12", "price": 32000, "description": "Action camera with 5.3K video recording", "stock": 7},
    {"id": 24, "name": "DJI Mini 4 Pro", "price": 95000, "description": "Compact professional camera drone", "stock": 4},
    {"id": 25, "name": "Apple Watch Series 10", "price": 28000, "description": "Smartwatch with health and fitness tracking", "stock": 13},
    {"id": 26, "name": "Samsung Galaxy Watch 7", "price": 22000, "description": "Smartwatch with fitness monitoring", "stock": 10},
    {"id": 27, "name": "Garmin Forerunner 265", "price": 40000, "description": "Advanced GPS running smartwatch", "stock": 6},
    {"id": 28, "name": "Anker PowerCore", "price": 4500, "description": "Portable power bank with fast charging", "stock": 25},
    {"id": 29, "name": "Samsung T7 SSD", "price": 12000, "description": "Portable 1TB external solid state drive", "stock": 16},
    {"id": 30, "name": "SanDisk Ultra USB", "price": 1500, "description": "64GB USB flash drive", "stock": 30},

    {"id": 31, "name": "Nike Air Force 1", "price": 12000, "description": "Classic everyday sneakers", "stock": 20},
    {"id": 32, "name": "Nike Air Jordan 1", "price": 18000, "description": "Iconic basketball sneakers", "stock": 15},
    {"id": 33, "name": "Adidas Ultraboost", "price": 16000, "description": "Comfortable running shoes", "stock": 12},
    {"id": 34, "name": "Nike Pegasus 41", "price": 14000, "description": "Daily running shoes with responsive cushioning", "stock": 18},
    {"id": 35, "name": "Adidas Predator", "price": 11000, "description": "Professional football boots", "stock": 9},
    {"id": 36, "name": "Puma Future", "price": 10000, "description": "Football boots for agility and control", "stock": 11},
    {"id": 37, "name": "Nike Training Shirt", "price": 2500, "description": "Lightweight breathable training shirt", "stock": 35},
    {"id": 38, "name": "Adidas Tracksuit", "price": 7500, "description": "Comfortable sports tracksuit", "stock": 14},
    {"id": 39, "name": "Under Armour Hoodie", "price": 6000, "description": "Warm athletic hoodie", "stock": 17},
    {"id": 40, "name": "Nike Running Shorts", "price": 3000, "description": "Lightweight running shorts", "stock": 28},

    {"id": 41, "name": "Wilson Basketball", "price": 4500, "description": "Official size indoor and outdoor basketball", "stock": 20},
    {"id": 42, "name": "Spalding NBA Ball", "price": 5500, "description": "Premium basketball with durable grip", "stock": 13},
    {"id": 43, "name": "Nike Football", "price": 4000, "description": "Durable football for training and matches", "stock": 22},
    {"id": 44, "name": "Adidas Football", "price": 5000, "description": "High quality match football", "stock": 16},
    {"id": 45, "name": "Wilson Tennis Racket", "price": 9000, "description": "Professional tennis racket", "stock": 8},
    {"id": 46, "name": "Babolat Pure Drive", "price": 15000, "description": "Advanced tennis racket for powerful shots", "stock": 5},
    {"id": 47, "name": "Yonex Badminton Racket", "price": 7000, "description": "Lightweight badminton racket", "stock": 10},
    {"id": 48, "name": "Speedo Swimming Goggles", "price": 1800, "description": "Anti fog swimming goggles", "stock": 25},
    {"id": 49, "name": "Speedo Swim Cap", "price": 900, "description": "Comfortable silicone swimming cap", "stock": 30},
    {"id": 50, "name": "Arena Swimming Suit", "price": 6500, "description": "Professional swimming training suit", "stock": 12},

    {"id": 51, "name": "Adjustable Dumbbells", "price": 18000, "description": "Adjustable weight dumbbells for home workouts", "stock": 7},
    {"id": 52, "name": "Olympic Barbell", "price": 14000, "description": "Heavy duty barbell for strength training", "stock": 6},
    {"id": 53, "name": "Weight Plates Set", "price": 12000, "description": "Set of weight plates for gym training", "stock": 9},
    {"id": 54, "name": "Resistance Bands", "price": 1500, "description": "Elastic resistance bands for fitness", "stock": 40},
    {"id": 55, "name": "Yoga Mat", "price": 2200, "description": "Non slip exercise and yoga mat", "stock": 25},
    {"id": 56, "name": "Foam Roller", "price": 1800, "description": "Massage roller for muscle recovery", "stock": 18},
    {"id": 57, "name": "Pull Up Bar", "price": 3500, "description": "Doorway pull up bar for home workouts", "stock": 11},
    {"id": 58, "name": "Kettlebell 16kg", "price": 5000, "description": "Cast iron kettlebell for functional training", "stock": 10},
    {"id": 59, "name": "Jump Rope", "price": 1000, "description": "Adjustable skipping rope for cardio", "stock": 35},
    {"id": 60, "name": "Gym Gloves", "price": 1600, "description": "Protective gloves for weightlifting", "stock": 20},

    {"id": 61, "name": "Boxing Gloves", "price": 5500, "description": "Training boxing gloves with wrist support", "stock": 14},
    {"id": 62, "name": "Punching Bag", "price": 13000, "description": "Heavy punching bag for boxing training", "stock": 5},
    {"id": 63, "name": "Boxing Hand Wraps", "price": 800, "description": "Protective hand wraps for boxing", "stock": 30},
    {"id": 64, "name": "MMA Shin Guards", "price": 4500, "description": "Protective shin guards for martial arts", "stock": 12},
    {"id": 65, "name": "Everlast Mouthguard", "price": 1200, "description": "Protective mouthguard for combat sports", "stock": 22},
    {"id": 66, "name": "Nike Training Shoes", "price": 11000, "description": "Stable shoes for gym workouts", "stock": 13},
    {"id": 67, "name": "Adidas Sport Backpack", "price": 3500, "description": "Spacious backpack for sports equipment", "stock": 18},
    {"id": 68, "name": "Nike Sports Bag", "price": 4000, "description": "Durable gym duffel bag", "stock": 16},
    {"id": 69, "name": "Under Armour Water Bottle", "price": 900, "description": "Reusable sports water bottle", "stock": 40},
    {"id": 70, "name": "Hydration Backpack", "price": 5000, "description": "Water carrying backpack for outdoor activities", "stock": 8},

    {"id": 71, "name": "Trekking Backpack", "price": 9500, "description": "Large backpack for hiking and camping", "stock": 9},
    {"id": 72, "name": "Hiking Boots", "price": 13000, "description": "Water resistant boots for mountain hiking", "stock": 10},
    {"id": 73, "name": "Camping Tent", "price": 15000, "description": "Two person waterproof camping tent", "stock": 6},
    {"id": 74, "name": "Sleeping Bag", "price": 6500, "description": "Insulated sleeping bag for outdoor camping", "stock": 12},
    {"id": 75, "name": "Trekking Poles", "price": 3500, "description": "Adjustable poles for hiking support", "stock": 15},
    {"id": 76, "name": "Mountain Bike Helmet", "price": 4500, "description": "Protective helmet for cycling", "stock": 17},
    {"id": 77, "name": "Road Bike", "price": 65000, "description": "Lightweight road bicycle for long distance cycling", "stock": 3},
    {"id": 78, "name": "Mountain Bike", "price": 55000, "description": "All terrain mountain bicycle", "stock": 4},
    {"id": 79, "name": "Cycling Gloves", "price": 1800, "description": "Padded gloves for comfortable cycling", "stock": 24},
    {"id": 80, "name": "Cycling Glasses", "price": 2500, "description": "UV protection sports sunglasses", "stock": 19},

    {"id": 81, "name": "Fitness Tracker", "price": 7000, "description": "Wearable device for daily activity tracking", "stock": 14},
    {"id": 82, "name": "Heart Rate Monitor", "price": 8500, "description": "Chest strap heart rate monitor", "stock": 9},
    {"id": 83, "name": "Smart Jump Rope", "price": 3000, "description": "Digital skipping rope with workout counter", "stock": 15},
    {"id": 84, "name": "Massage Gun", "price": 9000, "description": "Percussion massager for muscle recovery", "stock": 7},
    {"id": 85, "name": "Treadmill", "price": 85000, "description": "Electric treadmill for home cardio workouts", "stock": 3},
    {"id": 86, "name": "Exercise Bike", "price": 45000, "description": "Indoor stationary cycling machine", "stock": 5},
    {"id": 87, "name": "Elliptical Trainer", "price": 70000, "description": "Low impact cardio exercise machine", "stock": 2},
    {"id": 88, "name": "Gym Bench", "price": 11000, "description": "Adjustable weight training bench", "stock": 8},
    {"id": 89, "name": "Ab Roller", "price": 1200, "description": "Core training wheel for abdominal exercises", "stock": 30},
    {"id": 90, "name": "Push Up Bars", "price": 1500, "description": "Ergonomic handles for push up exercises", "stock": 25},

    {"id": 91, "name": "Smart Scale", "price": 4500, "description": "Digital body weight scale with Bluetooth", "stock": 12},
    {"id": 92, "name": "Sports Towel", "price": 800, "description": "Quick drying microfiber sports towel", "stock": 40},
    {"id": 93, "name": "Ankle Weights", "price": 2500, "description": "Adjustable ankle weights for fitness", "stock": 16},
    {"id": 94, "name": "Wrist Weights", "price": 2200, "description": "Lightweight wrist weights for training", "stock": 14},
    {"id": 95, "name": "Balance Board", "price": 4000, "description": "Balance training equipment for stability", "stock": 8},
    {"id": 96, "name": "Agility Ladder", "price": 1800, "description": "Speed and footwork training ladder", "stock": 20},
    {"id": 97, "name": "Cones Training Set", "price": 1200, "description": "Training cones for agility drills", "stock": 35},
    {"id": 98, "name": "Resistance Parachute", "price": 2800, "description": "Speed training parachute for sprinting", "stock": 10},
    {"id": 99, "name": "Hand Gripper", "price": 900, "description": "Adjustable hand strength training tool", "stock": 30},
    {"id": 100, "name": "Professional Sports Watch", "price": 18000, "description": "Digital sports watch with stopwatch and timer", "stock": 11}
]

def main():
    pr = sys.argv[1]
    res = ai(pr)
    print(res)

def database():
    dbc = psycopg.connect(
        host='localhost',
        port=7001,
        user='admin',
        password='BigMmd1392',
        dbname='testdb'
    )

    db = dbc.cursor()
    db.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price INT,
        description VARCHAR(1000) NOT NULL,
        stock INT
    );
    """)

    for product in products:
        db.execute("""
            INSERT INTO products (name, price, description, stock)
            VALUES (%s, %s, %s, %s)
        """, (
        product["name"],
        product["price"],
        product["description"],
        product["stock"]
        ))
    db.execute("SELECT * FROM products")
    et = db.fetchall()
    db.close()

    return et

def ai(prompt):
    load_dotenv()

    api_key=os.getenv("aikey")
    url = os.getenv("aiurl")

    client = QdrantClient(url=os.getenv('qdranturl'))
    ai = OpenAI(
        api_key=os.getenv('embaikey'),
        base_url=os.getenv('embaiurl')
    )
    datas = database()

    if client.collection_exists("products"):
        collection = client.get_collection("products")

    else:
        client.create_collection(
            collection_name="products",
            vectors_config=models.VectorParams(
                size=1536,
                distance=models.Distance.COSINE
            )
        )

    vectors = []
    for v in datas:
        id = v[0]
        name = v[1]
        price = v[2]
        description = v[3]

        aboutv = f'{name}, {description}. the cost is {price}.'
        response = ai.embeddings.create(
        input=aboutv, model="text-embedding-3-small"
        )

        em = response.data[0].embedding
        client.upsert(
            collection_name="products",
            points=[
                models.PointStruct(
                    id=id,
                    vector=em,
                    payload={
                        "name": name,
                        "price":price,
                        "description":description
                    }
                )
        ]
    )

    res = ai.embeddings.create(
        input=prompt, model="text-embedding-3-small"
    )   
    search_embed = res.data[0].embedding   

    search_res = client.query_points(
        collection_name="products",
        query=search_embed,
        limit=20,
        with_payload=True
    )

    if search_res.points:
        etelaat = search_res.points[0].payload

    else:
        etelaat = 'nothing'

    about = f"""
    you are a ai for a store you're goal is helping to people to buy what they want if they're question was about the product and buying things
    .if users question was about product try to use two or three of these : {etelaat}
    """
    print(etelaat)

    heade = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {api_key}'
        }
    body = {
            'model': "openai/gpt-5.4-nano",
            'messages': [
                {
                    'role': 'system',
                    'content': f'{about}'
                },
                {
                    'role': 'user',
                    'content': f'{prompt}'
                }
            ]
        }

    res = requests.post(url, json=body, headers=heade)
    return res.json()["choices"][0]["message"]["content"]

if __name__ == '__main__':
    main()


