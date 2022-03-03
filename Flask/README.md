# Dockerfile内でのセッティング

### ENV FLASK_RUN_PORT=5001
```
$ export FLASK_RUN_PORT=5001  

　　　(macOS Monterey のAirPlayとのコンフリクト回避)     
```
### ENV FLASK_ENV=development
```
　→　$ export FLASK_ENV=development  
　　　(デバックモードに設定)   
```
### ENV FLASK_APP=app
```
　→　$ export FLASK_APP=app   
　　　(起動アプリ：app.py)    
```
### 起動コマンド（コメントアウト）
```
$ flask run --host=0.0.0.0
```
 

# 
### 起動コマンドのオプションについて

```
$ flask run --host=0.0.0.0
```
- localhost:5001 にアクセスする。   
※127.0.0.1 では、ダンマリ。   

### ＜備考＞
- VScodeでattachの場合、   
"--host=0.0.0.0" をつけなくても、127.0.0.0:5001でアクセス可   
（実行時に表示されるリンクからアクセス可）  
- 共通化のためには、VScodeでattachした場合も  
"--host=0.0.0.0" をつけるのが良い