# cv2.imshow()のために
## mac
- XQuartz インストール
- xhost オープン（開放）
```
xhost + 
```

## コンテナ実行（docker run）

- .Xauthority のマウント
- 環境変数　DISPLAYの設定

<サンプル>
```
docker run -d -v /Users/sueno/OpenCV/Projects:/work -v /Users/sueno/.Xauthority:/root/.Xauthority -e DISPLAY=$(hostname):0 -p 8888:8888 --name opencv ubuntu-python38
```