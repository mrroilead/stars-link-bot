from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_i18n import I18nContext
from bot.core.config import config

router: Router = Router(name=__name__)

@router.message(Command("start"))
async def start_intro(message: Message, i18n: I18nContext) -> None:
    """Show startup products and discount info."""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"🤖 ChatGPT (<s>{config.PRODUCTS['chatgpt']['old_price']}</s> -> {config.PRODUCTS['chatgpt']['price']} ⭐)", callback_data="buy_chatgpt")],
        [InlineKeyboardButton(text=f"🎨 Midjourney (<s>{config.PRODUCTS['midjourney']['old_price']}</s> -> {config.PRODUCTS['midjourney']['price']} ⭐)", callback_data="buy_midjourney")],
        [InlineKeyboardButton(text=f"🛠 Creator Toolkit (<s>{config.PRODUCTS['creator']['old_price']}</s> -> {config.PRODUCTS['creator']['price']} ⭐)", callback_data="buy_creator")],
        [InlineKeyboardButton(text=f"📈 SEO & Marketing (<s>{config.PRODUCTS['seo']['old_price']}</s> -> {config.PRODUCTS['seo']['price']} ⭐)", callback_data="buy_seo")],
        [InlineKeyboardButton(text=f"🔬 Research Pack (<s>{config.PRODUCTS['research']['old_price']}</s> -> {config.PRODUCTS['research']['price']} ⭐)", callback_data="buy_research")],
    ])
    
    await message.answer(
        i18n.get("start", startup_name=config.STARTUP_NAME),
        reply_markup=keyboard,
        parse_mode="HTML"
    )
