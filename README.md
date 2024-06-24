# chat-widget 💬

Public Chat Widget 💬 from Mesolitica!

## how-to

### localhost

Use Python webserver,

```bash
python3 server.py --port 8080
```

### Existing website

```html
<script src="chat.js"></script>
<script>
ChatWidget.init('https://example.com', color = '#1076EE');
</script>
```