# uv-template

`uv` と `mise` で構成された Python プロジェクトテンプレートです。

## 🛠 前提条件
開発を始める前に、以下のツールがインストールされていることを確認してください:
- **mise**: 開発ツール・ランタイムマネージャー
- **uv**: 高速な Python パッケージ・プロジェクトマネージャー

## クイックスタート

### 1. リポジトリのクローン

```bash
git clone git@github.com:Kenshin0011/uv-template.git
cd uv-template
```

### 2. ランタイムのインストール (mise)

`.mise.toml` に定義された Python バージョンを自動でインストールします。

```bash
mise install
```

### 3. 仮想環境の作成と依存関係の同期 (uv)

```bash
mise exec -- uv sync
```

## 開発コマンド一覧

### アプリケーションの実行

```bash
mise exec -- uv run src/main.py
```

### コードの自動整形とチェック (ruff)

コードのスタイルを整え、潜在的なバグや不適切な記述をチェックします。

- コードの自動整形 (フォーマット):

```bash
mise exec -- uv run ruff format
```

- コードの静的解析 (リンターチェック):

```bash
mise exec -- uv run ruff check
```

- リンターによる自動修正の適用:

```bash
mise exec -- uv run ruff check --fix
```

### テストの実行
`pytest` を使用してテスト一式を実行します

```bash
mise exec -- uv run pytest
```

詳細なテスト結果やカバレッジを確認したい場合:

```bash
# 冗長表示モードで実行
mise exec -- uv run pytest -v
```

### 開発用パッケージ(pytest等)の追加方法

```bash
mise exec -- uv add --dev pytest
```
