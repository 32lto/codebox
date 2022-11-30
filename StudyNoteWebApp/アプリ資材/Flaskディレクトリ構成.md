# uwsgi/Flaskディレクトリ構成  
  
## 現状の構成  
  
/var/www/uwsgi配下
|-- emperor.ini
|-- flask_app
|   |-- application.py
|   |-- models
|   |   |-- __init__.py
|   |-- static
|   |   |-- css
|   |   |   |-- stepbar.css
|   |   |   `-- style.css
|   `-- templates
|       |-- layout.html
|       `-- welcome.html
|-- sockets
|   `-- pcg.sock
`-- vassals
    `-- parallelgame.net.ini
  
※参考：https://qiita.com/shixukeizai/items/49f6dbccf5364e8fb499  
  
