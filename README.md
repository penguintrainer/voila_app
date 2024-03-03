## 概要
今回画像処理を行うにあたって、マスク処理や矩形選択結果をjson形式で吐き出せるとよかったので、そのための簡単なwebアプリケーションを公開。

## ディレクトリ構造
```bash
├─ README.md
├─ doc
│  └─ setup.md
├─ test
│   └─ ......
└─ app
   ├─ main.py
   ├─ notebook
   │   ├─ main.ipynb
   │   ├─ image.ipynb
   │   ├─ PyCaret.ipynb
   │   └─ ......
   ├─ img
   │   ├─ sample.png
   │   └─ ......
   ├─ icon
   │   ├─ icon.png
   │   └─ ......
   ├─ config
   │   ├─ app_confg.json
   │   ├─ mask
   │   │   ├─ mask01.json
   │   │   ├─ ......
   │   │   └─ ......
   │   ├─ area
   │   │   ├─ area01.json
   │   │   ├─ ......
   │   │   └─ ......
   │   └─ ......
   ├─ utils
   │   ├─ ui.py
   │   ├─ cv.py
   │   ├─ exceptions.py
   │   └─ ......
   └─ ......
```

### 使い方
```bash
.venv\Script\Activate
python .app\main.py
```
上記のようにメインプログラムを実行することで、voilaによるwebアプリケーションへの変換作業が開始し、ローカルホストを対象にwebブラウザが立ち上がる。

## 環境構築について
こちらの[ドキュメント](./doc/setup.md)にまとめている。

## 詳細
### voilaを使ってjupyter notebookをwebアプリについて
[voila](https://github.com/voila-dashboards/voila)とは
ipywidgetsによって書かれたjupyter notebokをwebアプリに変換してくれるライブラリ。
webアプリなのでデプロイすればほかのPCからも使用可能。

ipywidgetsで作成されるボタンやバーを使用することでそれらの表示をアプリケーション上でも使用可能になる。
どんなUIを作成可能であるかは[Widget List](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html)を参考にしてほしい。

その他、もう少しUI表示に特化したライブラリとしては[bqplot](https://bqplot.github.io/bqplot/)がある。

画像処理については、
[opencv-python](https://github.com/opencv/opencv-python)
有名な画像処理のライブラリであり、python以外の言語にも対応している
処理の例が集まっているリポジトリ[learnopencv](https://github.com/spmallick/learnopencv)

その他pythonで用いられる有名な画像処理ライブラリ
[Pillow](https://pillow.readthedocs.io/en/stable/)
[scikit-image](https://scikit-image.org/)