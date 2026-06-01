import logging
import os
import json
from pathlib import Path
from dotenv import load_dotenv

logger: logging.Logger = logging.getLogger(__name__)

class Config:
    def __init__(self) -> None:
        # Load .env if it exists, but don't fail if it doesn't (Railway uses direct env vars)
        self.BASE_DIR = Path(__file__).resolve().parents[2]
        env_path: Path = self.BASE_DIR / ".env"
        if env_path.exists():
            load_dotenv(env_path)

        self.BOT_TOKEN = os.getenv("BOT_TOKEN")
        if not self.BOT_TOKEN:
            logger.error("CRITICAL: BOT_TOKEN not found in environment variables!")

        self.STARTUP_NAME = os.getenv("STARTUP_NAME", "TopPromptBot")
        
        # Load products from JSON
        self.PRODUCTS = {}
        json_path = self.BASE_DIR / "product_packs.json"
        
        if json_path.exists():
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data.get('products', []):
                        # Map JSON structure to bot's expected product structure
                        # We use 'en' title by default for the internal key/ID
                        self.PRODUCTS[item['id']] = {
                            "title": item['titles'].get('en', item['id']),
                            "price": item['price_stars'],
                            "delivery_type": "text",
                            "content": "Placeholder: Your purchased prompt pack content will be here soon!"
                        }
                logger.info(f"Loaded {len(self.PRODUCTS)} products from product_packs.json")
            except Exception as e:
                logger.error(f"Error loading product_packs.json: {e}")
        
        # Fallback if JSON loading fails
        if not self.PRODUCTS:
            logger.warning("Using fallback hardcoded products")
            self.PRODUCTS = {
                "starter-creator-pack": {
                    "title": "Starter Creator Pack",
                    "price": 99,
                    "delivery_type": "text",
                    "content": "Welcome to your Starter Creator Pack! Here are your prompts: ..."
                }
            }

config: Config = Config()
