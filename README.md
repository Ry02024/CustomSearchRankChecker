# CustomSearchRankChecker
**注意: このREADMEは現在更新中です。最新情報は順次追加される予定です。**  
CustomSearchRankCheckerは、Googleカスタム検索APIを使用して特定のURLが複数のキーワードに対してどのようなランキングを持っているかをチェックするためのStreamlitアプリケーションです。このツールは、SEOの目的で、選択したキーワードに対するウェブサイトの検索エンジンランキングのポジションをモニタリングするのに役立ちます。

# 特徴
Google APIキーとカスタム検索エンジンIDの入力
ターゲットURLとキーワードの指定
取得する検索結果の最大件数の設定（デフォルトは30件、最大100件まで設定可能）
指定されたURLのキーワードランキングを表示
インストール
リポジトリをクローンします:

bash
```コードをコピーする
git clone https://github.com/yourusername/KeywordRankChecker.git
cd KeywordRankChecker
```
必要な依存関係をインストールします:

bash
```コードをコピーする
pip install -r requirements.txt
```
使用方法
Streamlitアプリケーションを実行します:

bash
```コードをコピーする
streamlit run streamlit_app.py
```
ウェブブラウザを開き、ローカルのStreamlitサーバー（通常は http://localhost:8501）にアクセスします。

以下の手順に従います:

Google APIキーとカスタム検索エンジンIDを入力します。
有効な入力が確認された後、ターゲットURLとキーワード（カンマ区切り）を入力します。
取得する検索結果の最大件数を設定します（デフォルトは30件）。
「検索」ボタンをクリックしてランキングを確認します。
ファイル構成
arduino
```コードをコピーする
KeywordRankChecker/
├── fetch.py
├── ranking.py
├── display.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```
fetch.py: Googleカスタム検索APIから検索結果を取得する関数が含まれています。
ranking.py: 指定されたURLのキーワードランキングをチェックする関数が含まれています。
display.py: Streamlitアプリでランキングを表示する関数が含まれています。
streamlit_app.py: Streamlitアプリケーションのメインファイルです。
requirements.txt: プロジェクトに必要なPython依存関係が記載されています。
# 設定
アプリケーションを実行する前に、必要なAPIキーを用意してください:

Google APIキー
カスタム検索エンジンID
これらのキーはStreamlitのインターフェースを通じて入力します。

# ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細についてはLICENSEファイルを参照してください。

# 貢献
貢献は歓迎します！変更提案があれば、issueを開くか、プルリクエストを提出してください。

# 謝辞
Streamlit
Googleカスタム検索API
# バージョン
v1.0
初期リリース
Google APIキーとカスタム検索エンジンIDの入力
ターゲットURLとキーワードの指定
最大100件までの検索結果取得設定
検索結果のランキング表示

このREADMEをコピーして、プロジェクトのルートディレクトリにREADME.mdとして保存してください。また、以下の内容でrequirements.txtファイルも作成してください：
