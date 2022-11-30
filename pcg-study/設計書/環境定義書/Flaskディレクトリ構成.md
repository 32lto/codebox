# uwsgi/Flaskディレクトリ構成  
  
## 現状の構成  
  
/var/www/uwsgi配下
|-- emperor.ini
|-- flask_app
|   |-- application.py
|   |-- db.py
|   |-- models
|   |   |-- __init__.py
|   |   `-- rankings.py
|   |-- static
|   |   |-- css
|   |   |   |-- stepbar.css
|   |   |   `-- style.css
|   |   |-- game
|   |   |   |-- magicNumber
|   |   |   |   |-- Build
|   |   |   |   |   |-- UnityLoader.js
|   |   |   |   |   |-- result_Sudoku.data.unityweb
|   |   |   |   |   |-- result_Sudoku.json
|   |   |   |   |   |-- result_Sudoku.wasm.code.unityweb
|   |   |   |   |   `-- result_Sudoku.wasm.framework.unityweb
|   |   |   |   `-- TemplateData
|   |   |   |       |-- UnityProgress.js
|   |   |   |       |-- favicon.ico
|   |   |   |       |-- fullscreen.png
|   |   |   |       |-- progressEmpty.Dark.png
|   |   |   |       |-- progressEmpty.Light.png
|   |   |   |       |-- progressFull.Dark.png
|   |   |   |       |-- progressFull.Light.png
|   |   |   |       |-- progressLogo.Dark.png
|   |   |   |       |-- progressLogo.Light.png
|   |   |   |       |-- style.css
|   |   |   |       `-- webgl-logo.png
|   |   |   `-- tako
|   |   |       |-- Build
|   |   |       |   |-- UnityLoader.js
|   |   |       |   |-- WebGL.data.unityweb
|   |   |       |   |-- WebGL.json
|   |   |       |   |-- WebGL.wasm.code.unityweb
|   |   |       |   `-- WebGL.wasm.framework.unityweb
|   |   |       `-- TemplateData
|   |   |           |-- UnityProgress.js
|   |   |           |-- favicon.ico
|   |   |           |-- fullscreen.png
|   |   |           |-- progressEmpty.Dark.png
|   |   |           |-- progressEmpty.Light.png
|   |   |           |-- progressFull.Dark.png
|   |   |           |-- progressFull.Light.png
|   |   |           |-- progressLogo.Dark.png
|   |   |           |-- progressLogo.Light.png
|   |   |           |-- style.css
|   |   |           `-- webgl-logo.png
|   |   |-- image
|   |   |   |-- game_image_comingsoon.png
|   |   |   |-- game_image_mahojin.png
|   |   |   `-- game_image_takokuso.png
|   |   |-- js
|   |   `-- json
|   `-- templates
|       |-- contact.html
|       |-- game
|       |   |-- magicNumber.html
|       |   `-- tako.html
|       |-- layout.html
|       |-- ranking.html
|       `-- welcome.html
|-- sockets
|   `-- pcg.sock
`-- vassals
    `-- parallelgame.net.ini
  
※参考：https://qiita.com/shixukeizai/items/49f6dbccf5364e8fb499  
  
