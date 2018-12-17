path=$(pwd)
echo $path

mkdir -p $path/ws_py/
sudo rsync -av --delete ~/src/websocket/ws_py $path
