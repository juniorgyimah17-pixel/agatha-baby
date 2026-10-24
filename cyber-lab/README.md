# Two-Phone Call-Log Consent Lab

Authorized Android lab for learning permissions, client/server communication, and data transmission.

**Phone A:** run `receiver/server.py` on the private LAN.

**Phone B:** install the Android app, grant `READ_CALL_LOG` when Android asks, and press the explicit consent button.

Receiver configured for the current LAN address:

`http://10.119.176.166:8080/upload`

Use only with the device owner's informed consent. Keep the receiver on a private network and do not expose it to the public internet.

## Receiver

```bash
pip install -r requirements.txt
python server.py
```

Then open `http://10.119.176.166:8080/` from a browser on the same network.
