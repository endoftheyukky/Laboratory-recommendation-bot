# Laboratory Recommendation Bot

## 概要
このChatBotは法政大学情報科学部の研究室を推薦するために開発されました。Pythonと`chatbotweb`というライブラリを使用して実装されています。このBotは、研究室に関連するキーワードとユーザーからの質問に基づいて最も適した研究室を推薦します。

## 特徴
- **リアルタイムの研究室情報**: [法政大学の研究室情報ページ](https://nyushi.hosei.ac.jp/laboratory/faculty/1)から`beautifulSoup`と`requests`を使ってスクレイピングしたデータを使用。
- **自然言語処理の活用**: ユーザーの入力から重要なキーワードを抽出するために、日本語の形態素解析器である`Janome`を使用。
- **スコアリング方式**: ユーザーの興味に基づいて各研究室にスコアを割り当て、最適な研究室を推薦。

## インストール方法
1. 必要なライブラリをインストール:
    ```bash
    pip install beautifulsoup4
    pip install requests
    pip install janome
    ```

2. GitHubからリポジトリをクローン:
    ```bash
    git clone [リポジトリURL]
    ```

3. スクリプトを実行:
    ```bash
    cd [クローンしたディレクトリ]
    python [スクリプトのファイル名]
    ```

## 注意点
- このコードは改善の余地があります。可読性の向上を目指して今後更新される予定です。

## ライセンス
[ここにライセンス情報を記載]

## 著者
[あなたの名前や連絡先]
