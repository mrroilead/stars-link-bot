import logging
from aiogram import Bot, F, Router, html, types
from aiogram.filters import Command
from aiogram.types import Message, PreCheckoutQuery, LabeledPrice, CallbackQuery
from aiogram_i18n import I18nContext
from bot.core.config import config

router: Router = Router(name=__name__)
logger = logging.getLogger(__name__)

@router.callback_query(F.data.startswith("buy_"))
async def process_buy_callback(callback: CallbackQuery, bot: Bot, i18n: I18nContext):
    product_key = callback.data.split("_")[1]
    product = config.PRODUCTS.get(product_key)
    
    if not product:
        await callback.answer("Product not found")
        return

    await bot.send_invoice(
        chat_id=callback.message.chat.id,
        title=product['title'],
        description=f"Get instant access to {product['title']}. Special discount active!",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label="⭐ Premium Access", amount=product['price'])],
        payload=f"product_{product_key}",
        start_parameter=f"buy_{product_key}"
    )
    await callback.answer()

@router.pre_checkout_query()
async def handle_pre_checkout(pre_checkout_query: PreCheckoutQuery, bot: Bot) -> None:
    """Approve Stars pre-checkout queries."""
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@router.message(F.successful_payment)
async def handle_successful_payment(message: Message, i18n: I18nContext) -> None:
    """Notify user about successful Stars payment and deliver links."""
    info = message.successful_payment
    payload = info.invoice_payload
    
    product_key = payload.split("_")[1] if "_" in payload else "chatgpt"
    product = config.PRODUCTS.get(product_key, config.PRODUCTS['chatgpt'])
    
    links_text = "\n".join([f"• {link}" for link in product['links']])
    
    # Log successful payment
    logger.info(f"SUCCESSFUL_PAYMENT: user_id={message.from_user.id}, product={product_key}, amount={info.total_amount}, charge_id={info.telegram_payment_charge_id}")
    
    await message.reply(
        i18n.get(
            "payment-success",
            startup_name=config.STARTUP_NAME,
            links=links_text,
            transaction_id=html.quote(info.telegram_payment_charge_id),
        ),
        parse_mode="HTML"
    )
