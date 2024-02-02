## Quick Start

First, download the source code, create a virtual environment, and install dependencies.

```bash
git clone https://github.com/briceyan/frame-app-examples
cd frame-app-examples/gm
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Validate your Frame app in a development environment.

```bash
python -m flask --app api.index run
```

Visit http://localhost:5000 to see the result.

## Testing

Make sure your app is publicly accessible before deploying it. You can use ngrok to forward external requests to your local deployment.

```bash
ngrok http 5000
```

Ensure you are adhering to the Frame app protocol.

- [Frame App Protocol](https://warpcast.com/~/developers/frames)

## Deployment

Deploy using the following command:

```bash
vercel deploy
```
