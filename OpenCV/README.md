# macOS for imgshow()

- XQuartz インストール
- xhost オープン（開放）
```
xhost + 
```

# イメージ作成 (docker build)
```
docker build -t python-opencv .
```
# コンテナ作成 (docker run)
## macOS

- .Xauthority のマウント
- 環境変数　DISPLAYの設定

jupyter lab 起動
```
docker run -d -v $PWD/Projects:/work -v ~/.Xauthority:/root/.Xauthority -e DISPLAY=$(hostname):0 -p 8888:8888 --name python-opencv python-opencv
```
コマンドプロンプトを起動し、コマンドラインからテストする場合 （使用後、削除）
```
docker run --rm -it -v $PWD/Projects:/work -v ~/.Xauthority:/root/.Xauthority -e DISPLAY=$(hostname):0 -p 8888:8888 python-opencv bash
```

## ubuntu 

```
docker run -d -v $PWD/Projects:/work -v /tmp/.X11-unix:/tmp/.X11-unix:rw  -e DISPLAY=:0 -e QT_X11_NO_MITSHM=1 -p 8888:8888 --name python-opencv python-opencv
```

# 調べたトラブル対策 (主にubuntu)
- library不足 ？  
pyqt5
- python package 不足？  
　a案) python-pyqt5 / pyqt5-dev-tools / qttools5-dev-tools  
　b案) libxcb-xinerama0
以下、参考
```
docker run -it \
    --user=$(id -u):$(id -g) \  
    # ホスト側のUIDとGIDでコンテナを起動
    $(for i in $(id -G); do echo -n "--group-add "$i; done) \  
    # 所属しているグループを全て設定
    --env=DISPLAY=$DISPLAY \  # ホスト側のDISPLAYを設定
    --env=QT_X11_NO_MITSHM=1 \  # X errorを抑える
    --workdir="/home/$USER" \  
    # 初期ディレクトリをホストユーザーのホームに設定
    --volume="/home/$USER:/home/$USER" \  
    # ホストユーザーホームをマウント
    --volume="/etc/group:/etc/group:ro" \  
    # 以下4つはホスト側のユーザー情報をそのまま使うための設定
    --volume="/etc/passwd:/etc/passwd:ro" \
    --volume="/etc/shadow:/etc/shadow:ro" \
    --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \  
    # ホスト側のXを使う
    osrf/ros:indigo-desktop-full \  
    # Dockerコンテナを指定
    rqt  # 実行コマンドを指定
```

```
$ docker run -it \
             --privileged \
             --env="DISPLAY=$DISPLAY" \
             --env=QT_X11_NO_MITSHM=1 \  
             --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
             --volume="$HOME/ws/:/home/" \
             --name="ubuntu_cv2" \
             ubuntu:18.04
```