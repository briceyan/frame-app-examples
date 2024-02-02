## Quick Start

Create a virtual environment and install dependencies.

```bash
cd frame-app-examples/gm-universe
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run your frame app locally before deploying it to production.

```bash
python -m flask --app api.index run
```

Visit http://localhost:5000 to check.

## Testing

Make sure your app is publicly accessible before deploying it. You can use ngrok to forward external requests to your local deployment.

```bash
ngrok http 5000
```

Ensure you are adhering to the Frame app protocol.

- [Frame App Protocol](https://warpcast.com/~/developers/frames)

## Deployment

If all goes well, deploy using the following command:

```bash
vercel deploy
```
