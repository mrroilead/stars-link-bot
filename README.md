<div align="center">
   <img src="files/stars.svg" alt="TopPromptBot Logo" width="140" height="140" style="border-radius:24px; box-shadow:0 4px 12px rgba(0,0,0,0.25);">

   <h1 style="margin-top: 24px; font-size:42px;">TopPromptBot - Startup MVP</h1>

   <p style="font-size:18px; color:#555; max-width:640px; line-height:1.4;">
      <strong>Premium AI Prompt Store powered by Telegram Stars ⭐</strong>
   </p>
</div>

---

## Startup MVP: TopPromptBot

This bot is a ready-to-use storefront for selling AI prompt packs, productivity libraries, and creator toolkits using **Telegram Stars (XTR)**.

### Features
- 🚀 **Instant Access**: Users get links immediately after successful payment.
- 💰 **Stars Only**: Uses native Telegram Stars currency (XTR) for a seamless UX.
- 🔥 **Discount Logic**: Integrated "50% Discount" messaging to drive conversions.
- 📦 **Product Catalog**: Pre-configured with ChatGPT, Midjourney, SEO, and Research packs.
- 📝 **Logging**: Successful payments are logged to the console/file for tracking.

### Configuration

To change prices, links, or the startup name, edit the following files:

1. **`.env`**:
   - `BOT_TOKEN`: Your Telegram Bot Token from @BotFather.
   - `STARTUP_NAME`: The name of your startup.

2. **`bot/core/config.py`**:
   - Edit the `PRODUCTS` dictionary to change titles, prices (original and discounted), and the links delivered after payment.

3. **`locales/en/messages.ftl`**:
   - Edit the text for the `/start` message, success message, and discount banners.

### Deployment

#### Local Run
```bash
pip install -r requirements.txt
python main.py
```

#### Production (PaaS like Railway/Render)
The repository includes a `Procfile` and `runtime.txt` for quick deployment.
1. Connect your GitHub fork to the PaaS.
2. Set the `BOT_TOKEN` and `STARTUP_NAME` environment variables in the PaaS dashboard.
3. The bot will start automatically using `python main.py`.

---

## Commands
- `/start`: Open the store and view available prompt packs.

---

<div align="center" style="margin-top:32px;">
   <p><strong>TopPromptBot MVP</strong></p>
   <p>Built with aiogram 3.x and Telegram Stars ⭐</p>
</div>
