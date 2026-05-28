import logging
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

logger: logging.Logger = logging.getLogger(__name__)

class Config:
    def __init__(self) -> None:
        env_path: Path = Path(__file__).resolve().parents[2] / ".env"

        if not env_path.exists():
            logger.error(".env file not found!")
            sys.exit(1)

        load_dotenv(env_path)

        if not os.getenv("BOT_TOKEN"):
            logger.error("Missing required env variable: BOT_TOKEN")
            sys.exit(1)

        self.BOT_TOKEN: str = os.getenv("BOT_TOKEN")
        self.STARTUP_NAME: str = os.getenv("STARTUP_NAME", "toppromptbot")
        
        # Products and prices
        self.PRODUCTS = {
            "chatgpt": {
                "title": "Ultimate ChatGPT Prompt Library",
                "price": 49,
                "old_price": 99,
                "links": [
                    "https://www.aiprm.com/",
                    "https://www.aiprm.com/prompts/",
                    "https://www.aiprm.com/en-gb/prompts/",
                    "https://prompts.chat/",
                    "https://github.com/bigscience-workshop/promptsource"
                ]
            },
            "midjourney": {
                "title": "Midjourney Mega Prompt Pack",
                "price": 74,
                "old_price": 149,
                "links": [
                    "https://prompthero.com/",
                    "https://promptbase.com/",
                    "https://www.aipromptlibrary.app/vs/prompthero"
                ]
            },
            "creator": {
                "title": "AI Creator Toolkit",
                "price": 99,
                "old_price": 199,
                "links": [
                    "https://flowgpt.com/",
                    "https://prompts.chat/",
                    "https://www.aiprm.com/"
                ]
            },
            "seo": {
                "title": "SEO + Marketing Prompt Vault",
                "price": 124,
                "old_price": 249,
                "links": [
                    "https://www.aiprm.com/prompts/",
                    "https://www.aiprm.com/",
                    "https://flowgpt.com/"
                ]
            },
            "research": {
                "title": "Prompt Engineering Research Pack 2026",
                "price": 149,
                "old_price": 299,
                "links": [
                    "https://promptflow.digital/prompts",
                    "https://www.reddit.com/r/PromptEngineering/comments/1sjgwd1/i_organized_200_prompts_by_use_case_into_a_free/",
                    "https://www.reddit.com/r/PromptEngineering/comments/1s9n81b/i_tested_500_ai_prompts_across_10_categories_here/",
                    "https://www.reddit.com/r/PromptEngineering/comments/1sglnor/i_tested_120_claude_prompt_patterns_over_3_months/",
                    "https://www.reddit.com/r/PromptCentral/comments/1rkqu0w/i_tested_600_ai_prompts_across_12_categories_over/"
                ]
            }
        }

config: Config = Config()
