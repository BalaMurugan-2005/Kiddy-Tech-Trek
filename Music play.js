<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fun Music for Kids</title>
    <style>
        body {
            text-align: center;
            background-color: #fce4ec;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #ff4081;
        }
        .instrument {
            display: inline-block;
            margin: 20px;
            padding: 20px;
            border: 2px solid #ff4081;
            border-radius: 10px;
            background-color: #fff;
            cursor: pointer;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <h1>Welcome to Fun Music for Kids!</h1>
    <div class="instrument" onclick="playSound('piano.mp3')">🎹 Play Piano</div>
    <div class="instrument" onclick="playSound('guitar.mp3')">🎸 Play Guitar</div>
    <div class="instrument" onclick="playSound('drum.mp3')">🥁 Play Drums</div>
    
    <script>
        function playSound(soundFile) {
            let audio = new Audio(soundFile);
            audio.play();
        }
    </script>
</body>
</html>
