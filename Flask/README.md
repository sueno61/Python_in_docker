# Dockerfile内でのセッティング

### ENV FLASK_RUN_PORT=5001
(macOS Monterey のAirPlayとのコンフリクト回避)     
```
export FLASK_RUN_PORT=5001  
```

### ENV FLASK_ENV=development
(デバックモードに設定)   
```
export FLASK_ENV=development  
```

### ENV FLASK_APP=app
(起動アプリ：app.py)    
```
export FLASK_APP=app   
```
### 起動コマンド（コメントアウト）
```
flask run --host=0.0.0.0
```
 

# 
## 起動コマンドのオプションとアクセス方法

### localhost:5001 にアクセスする。
※ "127.0.0.1:5001" では「ダンマリ」になる   

### ＜備考＞
- VScodeでattachの場合、   
"--host=0.0.0.0" をつけなくても、127.0.0.0:5001でアクセス可   
（実行時に表示されるリンクからアクセス可）  
- 共通化のためには、VScodeでattachした場合も  
"--host=0.0.0.0" をつけるのが良い