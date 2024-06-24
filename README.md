# chat-widget 💬

Chat Widget from Mesolitica!

- Fullscreen button and animation.
- Waiting chat animation.
- Customize color.
- Custom POST request.
- Auto generate user UUID and store the historical chats in UserSession.
- 100% pure vanilla Javascript.

https://github.com/mesolitica/chat-widget/assets/19810909/bd4220a9-38e4-4c6c-ac87-ba5788ead9d7

## how-to

### localhost

Use Python webserver,

```bash
python3 server.py --port 8080
```

### Existing website

Minimal as,

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>

  <script src="https://cdn.jsdelivr.net/gh/mesolitica/chat-widget/chat.js"></script>
  <script>
    ChatWidget.init(
      'https://example.com',
      color = '#1076EE',
      first_message = 'Hi, my name is bot!',
    );
  </script>
</body>

</html>
```

