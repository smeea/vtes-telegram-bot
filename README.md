# vtes-telegram-bot
VTES telegram card image bot - answers with card image if message in chat (direct or group) match full or partially with card name.

Active privacy-respecting & ad-free (keep no logs / don't send spam) telegram instance: `@VtesCardImageBot`.

# Deployment
Set your API TOKEN in `app.py`:
```
API_KEY = os.environ.get('API_KEY') or "PUT YOUR TOKEN HERE"
```
Run:
```
    uv run app.py
```
