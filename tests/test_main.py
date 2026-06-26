from main import main


def test_main_output(capsys):
    # main() 関数を実行
    main()

    # 標準出力をキャプチャ
    captured = capsys.readouterr()

    # 期待通りの出力（最後に改行が入るため \\n が必要）になっているか検証
    assert captured.out == "Hello from uv-template!\n"
