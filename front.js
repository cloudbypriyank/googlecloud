<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heygen Avatar Video</title>
</head>
<body>
    <div id="video-container">
        <h2>Create Your Avatar Video</h2>
        <textarea id="input-text" placeholder="Enter your script here..."></textarea>
        <button id="create-video-btn">Create Video</button>
        <div id="loading" style="display:none;">Processing your video...</div>
        <video id="avatar-video" controls style="display:none;"></video>
    </div>

    <script>
        const createVideoButton = document.getElementById('create-video-btn');
        const inputText = document.getElementById('input-text');
        const loadingIndicator = document.getElementById('loading');
        const videoElement = document.getElementById('avatar-video');

        createVideoButton.addEventListener('click', () => {
            const scriptText = inputText.value;

            createVideoButton.style.display = 'none';
            loadingIndicator.style.display = 'block';

            // Send a request to create the video
            fetch('/create_video', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    test: true,
                    caption: false,
                    width: 1920,
                    height: 1080,
                    character_type: "avatar",
                    character_scale: 1,
                    avatar_style: "normal",
                    avatar_id: "159c3167739842acb1644a4a985c950c",
                    input_text: scriptText,
                    voice_id: "0009aabefe3a4553bc581d837b6268cb"
                })
            })
            .then(response => response.json())
            .then(data => {
                const videoId = data.video_id;

                // Poll the status every 5 seconds
                const intervalId = setInterval(() => {
                    fetch(`/get_video_status/${videoId}`)
                    .then(response => response.json())
                    .then(statusData => {
                        if (statusData.status === 'ready') {
                            clearInterval(intervalId);
                            loadingIndicator.style.display = 'none';
                            videoElement.src = statusData.download_url;
                            videoElement.style.display = 'block';
                        }
                    });
                }, 5000);
            });
        });
    </script>
</body>
</html>
