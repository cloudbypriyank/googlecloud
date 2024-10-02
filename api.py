from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)
import logging
logging.basicConfig(level=logging.INFO)


HEYGEN_API_KEY = "MzAwYzdhMGMxMDcyNGU4ZjlhOGZkY2Q2YTdiZDk4NGMtMTcyNTg2NDY0MA=="

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create_video", methods=["POST"])
def create_video():
        # Receive video details from the frontend
        data = request.json
        
        url = "https://api.heygen.com/v2/video/generate"

        # Prepare payload from the received data
        payload = {
            "test": True,
            "caption": False,
            "dimension": {
                "width": 1280,
                "height": 720
            },
            "video_inputs": [
                {
                    "character": {
                        "type": "avatar",
                        "avatar_id": "159c3167739842acb1644a4a985c950c",
                        "avatar_style": "normal"
                    },
                    "voice": {
                        "type": "text",
                        "input_text": data.get("input_text", "Default text"),
                        "voice_id": "0009aabefe3a4553bc581d837b6268cb"
                    },
                    "background": {
                        "type": "color",
                        "value": "#008000"
                    }
                }
            ],
            "aspect_ratio": "16:9"
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-api-key": "MzAwYzdhMGMxMDcyNGU4ZjlhOGZkY2Q2YTdiZDk4NGMtMTcyNTg2NDY0MA=="
        }

        # Call Heygen API to create the video
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        
        # Return the response (including video_id) to the frontend
        response_json = response.json()
        video_id = response_json.get("data", {}).get("video_id")
        return jsonify({"video_id": video_id, "error": None})

@app.route("/get_video_status/<video_id>", methods=["GET"])
def get_video_status(video_id):
        # Check video status using the video ID
        url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
        
        headers = {
            "accept": "application/json",
            "x-api-key": HEYGEN_API_KEY
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 500

        print(response.text)  # Log the raw response
        return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)