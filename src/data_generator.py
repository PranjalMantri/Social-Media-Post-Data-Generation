import random
import faker
import numpy as np
from pprint import pprint

class ScalableContentGenerator:
    def __init__(self):
        self.faker = faker.Faker()
        self.post_types = ['carousel', 'reels', 'static_images']
        self.device_types = ['mobile phone', 'laptop']

        # Dynamic templates for captions
        self.caption_templates = {
            'travel': [
                "Exploring the beauty of {location}! 🌍✈️",
                "Every journey starts with a step in {location}.",
                "Wanderlust in {location}: the adventure continues!",
                "Traveling through {location}, finding new stories.",
                "Paradise found in {location}. 🌴✨"
            ],
            'fitness': [
                "Crushing goals at the {place}! 💪",
                "Every rep counts: {action} to greatness.",
                "No excuses, just {action} at the {place}.",
                "Feeling stronger at the {place}.",
                "It's a lifestyle, not a choice: {action} every day!"
            ],
            'food': [
                "Tasting the world, one bite at a time! 🍴",
                "Deliciousness overload: {dish} at {restaurant}.",
                "Good food, good mood. {dish} for the win!",
                "Exploring the flavors of {cuisine} cuisine. 🌮🍣",
                "Can’t resist this {dish}! 😋"
            ],
            'technology': [
                "Innovation at its finest with {device}. 💻📱",
                "The future is here: exploring {tech_trend}.",
                "Tech makes life easier. Check out {device}!",
                "Exploring the cutting-edge world of {tech_trend}.",
                "Stay connected, stay smart with {device}."
            ],
            'fashion': [
                "Stepping out in style with {brand}. 👗👠",
                "Today’s look: {style_adjective} and {style_adjective}.",
                "When in doubt, wear {color}!",
                "Dressed to impress with {brand}.",
                "Fashion is what you buy; style is what you do with it."
            ],
            'nature': [
                "Breathing in the fresh air of {location}. 🌲🌊",
                "Nature never goes out of style. 🌿",
                "Disconnect to reconnect in {location}.",
                "Every trail leads to a story in {location}.",
                "Embracing the beauty of {location}. 🌄"
            ]
        }

        # Dynamic hashtag pools
        self.hashtag_pools = {
            'travel': ['#Travel', '#Adventure', '#Explore', '#TravelGram', '#Wanderlust'],
            'fitness': ['#Fitness', '#Workout', '#GymLife', '#FitFam', '#HealthyLifestyle'],
            'food': ['#Foodie', '#Delicious', '#FoodLover', '#InstaFood', '#Yum'],
            'technology': ['#TechLife', '#Innovation', '#Gadgets', '#TechSavvy', '#Future'],
            'fashion': ['#OOTD', '#Style', '#Fashionista', '#Trendy', '#Chic'],
            'nature': ['#NatureLovers', '#Outdoors', '#Earth', '#Scenic', '#Wildlife']
        }

        # Common and trending hashtags
        self.trending_hashtags = [
            '#MondayMotivation', '#ThrowbackThursday', '#InstaGood', '#NoFilter', '#PhotoOfTheDay'
        ]

        # Words for dynamic placeholders
        self.places = ['gym', 'track', 'studio', 'outdoor park']
        self.actions = ['lifting', 'running', 'training', 'stretching']
        self.dishes = ['sushi', 'pasta', 'burger', 'tacos', 'salad']
        self.restaurants = ['Chez Gourmet', 'Urban Eats', 'Cafe Bliss', 'Food Haven']
        self.cuisines = ['Italian', 'Mexican', 'Japanese', 'Indian']
        self.tech_trends = ['AI', 'blockchain', 'VR', 'IoT']
        self.brands = ['Gucci', 'Zara', 'Nike', 'Adidas']
        self.style_adjectives = ['bold', 'chic', 'elegant', 'trendy']
        self.colors = ['red', 'blue', 'black', 'white']

    def generate_dynamic_caption(self, theme, geotag, device_type):
        template = random.choice(self.caption_templates[theme])
        caption = template.format(
            location=geotag,
            place=random.choice(self.places),
            action=random.choice(self.actions),
            dish=random.choice(self.dishes),
            restaurant=random.choice(self.restaurants),
            cuisine=random.choice(self.cuisines),
            device=device_type,
            tech_trend=random.choice(self.tech_trends),
            brand=random.choice(self.brands),
            style_adjective=random.choice(self.style_adjectives),
            color=random.choice(self.colors)
        )
        return caption

    def generate_dynamic_hashtags(self, theme):
        base_hashtags = random.sample(self.hashtag_pools[theme], k=3)
        # additional_hashtags = random.sample(self.trending_hashtags, k=2)
        return ' '.join(base_hashtags)

    def generate_engagement(self, views):
        likes = int(views * random.uniform(0.02, 0.05))
        comments = int(likes * random.uniform(0.1, 0.3))
        shares = int(comments * random.uniform(0.05, 0.2))
        return likes, comments, shares

    def generate_post_type_behavior(self, post_type):
        if post_type == 'reels':
            views = int(np.random.lognormal(mean=11, sigma=0.8))
        elif post_type == 'carousel':
            views = int(np.random.lognormal(mean=10, sigma=0.9))
        else:  # static_images
            views = int(np.random.lognormal(mean=9, sigma=1))
        return views

    def adjust_for_device(self, device_type, base_value):
        if device_type == 'mobile phone':
            return int(base_value * random.uniform(1.1, 1.5))
        else:
            return int(base_value * random.uniform(0.8, 1.2))

    def inject_anomaly(self, views):
        if random.random() < 0.05:  # 5% chance of being viral
            return views * random.uniform(10, 50)
        elif random.random() < 0.05:  # 5% chance of being underperforming
            return views * random.uniform(0.1, 0.5)
        return views

    def generate_post(self):
        theme = random.choice(list(self.caption_templates.keys()))
        post_type = random.choice(self.post_types)
        device_type = random.choice(self.device_types)
        geotag = self.faker.city()

        caption = self.generate_dynamic_caption(theme, geotag, device_type)
        hashtags = self.generate_dynamic_hashtags(theme)

        avg_wait_time = round(random.uniform(1.0, 15.0), 2)

        views = self.generate_post_type_behavior(post_type)
        views = self.inject_anomaly(views)
        likes, comments, shares = self.generate_engagement(views)
        likes = self.adjust_for_device(device_type, likes)

        post = {
            'post_id': self.faker.uuid4(),
            'post_type': post_type,
            'caption': caption,
            'hashtags': hashtags,
            'likes': likes,
            'comments': comments,
            'shares': shares,
            'views': views,
            "avg_wait_time": avg_wait_time,
            'geotag': geotag,
            'device_type': device_type
        }
        return post

    def generate_posts(self, num_posts):
        return [self.generate_post() for _ in range(num_posts)]

# Example usage
generator = ScalableContentGenerator()
posts = generator.generate_posts(1000)

# Print a few sample posts
for post in posts[:5]:
    pprint(post)
    print()
