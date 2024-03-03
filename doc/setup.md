## 環境構築に関するメモ書き
新しいPCで作業を新たに始めたので、私だったらこうやって環境構築するぞ
というメモ書き


## ソフトウェア開発環境のインストール
### VS code のインストール
多機能なテキストエディタ
[VS code](https://code.visualstudio.com/)

### gitのインストール
ソフトウェアのバージョン管理ソフト
後々使う、ソースコード共有に使われる[github](https://github.com/)を使うときにも使われる
[git](https://git-scm.com/downloads)


## pythonの実行環境のインストール
PCの本体へのインストールは下記の三つのみ
- pythonのインストール
- penvのインストール
- pipenvのインストール

その他のライブラリの導入などは各仮想環境毎に実行する

### pythonのインストール
プログラミング言語であるpythonのインストール
[公式サイト](https://www.python.org/)

### pyenvのインストール
一つのPCで複数のバージョンのpythonの実行環境を構築してくれるツール
[pyenv-win](https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#powershell)

### pipenvのインストール
一つのPCで複数の仮想環境を構築してくれるライブラリ
プロジェクト毎に実行環境を構築してくれる
[pipenv](https://pipenv-ja.readthedocs.io/)

仮想環境関係のフォルダをプロジェクトフォルダに格納するための設定
よくわからない場所()に、おっきなファイルが生成されるのを防ぐ
[PIPENV_VENV_IN_PROJECT](https://pipenv-ja.readthedocs.io/ja/translate-ja/advanced.html#pipenv.environments.PIPENV_VENV_IN_PROJECT)


## 仮想環境のセットアップ
### pipenvによるライブラリのインストール

```bash
pipenv install
```
