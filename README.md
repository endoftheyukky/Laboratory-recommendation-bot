# Laboratory-recommendation-bot

法政大学情報科学部の研究室を推薦するChatBotです。chatbotwebというライブラリを用いてPythonで実装しています。
判定に使用しているキーワードについては、[研究室情報の掲載されたサイト](https://nyushi.hosei.ac.jp/laboratory/faculty/1)をbeautifulSoupとrequestsを用いてスクレイピングした結果を使用しているため、研究室情報の更新にも対応しています。
スクレイピングして取得したキーワードと、その他の質問結果をもとにスコアリング方式を採用し、上位の研究室を推薦しています。

※コードの可読性に関しては欠ける部分がございますので、改善予定です。
