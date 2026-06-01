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
                        # Map new JSON schema to bot's expected product structure
                        # We use 'price_stars_sale' as the active price
                        self.PRODUCTS[item['id']] = {
                            "title": item.get('title_en', item['id']),
                            "price": item.get('price_stars_sale', item.get('price_stars_original', 99)),
                            "delivery_type": "links",
                            "content": item.get('prompt_links', ["https://github.com/mrroilead/stars-link-bot"])
                        }
                logger.info(f"Loaded {len(self.PRODUCTS)} products from product_packs.json")
            except Exception as e:
                logger.error(f"Error loading product_packs.json: {e}")
        
        # Fallback if JSON loading fails
        if not self.PRODUCTS:
            logger.warning("Using fallback hardcoded products")
            self.PRODUCTS = {
                "pack_01": {
                    "title": "Prompt Pack for Freelancers",
                    "price": 49,
                    "delivery_type": "links",
                    "content": ["https://github.com/mrroilead/stars-link-bot"]
                }
            }

config: Config = Config()
