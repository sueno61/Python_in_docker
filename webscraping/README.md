# ポイント
1. chromeとchromedriverのバージョンを合わせる
- google-chromeをインストールしたイメージでバージョンを確認
```
google-chrome --version
```
- バージョンに合わせたドライバーに指定変更（Dockerfile内）
```
ADD https://chromedriver.storage.googleapis.com/99.0.4844.51/chromedriver_linux64.zip /opt/chrome/
```

2. chromedriver のオプション指定
以下のオプションを追加
```
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
```

```
browser = webdriver.Chrome(chrome_options=options) 
```