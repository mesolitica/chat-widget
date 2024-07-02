# chat-widget 💬

Customizable Web Chat Widget 💬

## Features 🔥

- Collapse and expand animation.
- Fullscreen button and animation.
- Waiting chat respond animation.
- Customize color, title, font family and first message.
- Custom POST request.
- Auto generate user UUID and store the historical chats in UserSession.
- Error message on exception.
- 100% pure vanilla Javascript.

https://github.com/mesolitica/chat-widget/assets/19810909/bd4220a9-38e4-4c6c-ac87-ba5788ead9d7

## how-to

### localhost

Use Python webserver,

```bash
python3 server.py --port 8080 --host 0.0.0.0
```

### Existing website

Minimal as,

```html
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>

  <script src="https://cdn.jsdelivr.net/gh/mesolitica/chat-widget@0.1.1/chat.js"></script>
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

## Parameters

```js
window.ChatWidget = {
    init: function (
        url,
        color = "#0056FF",
        title = "Conversation",
        font_family = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
        first_message = "Hello, my name is bot!",
    ) {
        createChatWidget(url, color, title, font_family, first_message);
    }
};
```

## What kind of parameters we use for POST request?

```js
const jsonData = {
    sender: userUUID,
    message: text
};

fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(jsonData)
})
    .then(response => response.json())
    .then(data => {
        const r = data;
        removeTypingIndicator(typingIndicator);
        addMessage(r[0]['text'], 'ai');
    })
    .catch(error => {
        removeTypingIndicator(typingIndicator);
        addErrorMessage(error);
    });
```

The API must returned a single array with a dictionary element and `text` for the key.