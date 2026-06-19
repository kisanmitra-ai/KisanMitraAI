# KisanMitra AI App UI

Standalone mobile-first UI folder for the final KisanMitra AI welcome and onboarding screen.

Entry file:

```text
index.html
```

Assets:

```text
assets/kisanmitra-final-logo.png
assets/kisanmitra-welcome-reference.png
```

This folder is intentionally plain HTML/CSS/JS so it can later be wrapped with Capacitor, Cordova, React Native WebView, or another mobile shell without changing the approved UI design.

Backend save endpoint used by farmer registration:

```text
POST http://127.0.0.1:8010/api/mobile-app/farmer-register
```

The Supabase service key must stay in the backend `.env`; do not move it into this frontend folder.
