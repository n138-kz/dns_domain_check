import json
import argparse
import sys

# ANSIエスケープシーケンスによる文字色の定義
COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_RESET = "\033[0m"

# dnspython モジュールの存在チェック
try:
    import dns.resolver
except ModuleNotFoundError:
    print("=" * 70)
    print(f"{COLOR_RED}[ERROR]{COLOR_RESET} 'dnspython' ライブラリが見つかりません。")
    print("以下のいずれかの方法でライブラリをインストールしてください。")
    print("-" * 70)
    print("方法1: OSのパッケージマネージャーを使う場合 (Ubuntu / Debian等)")
    print("    sudo apt update")
    print("    sudo apt install python3-dnspython")
    print("-" * 70)
    print("方法2: 仮想環境 (venv) を作成して pip を使う場合 (推奨)")
    print("    python3 -m venv venv")
    print("    source venv/bin/activate")
    print("    pip install dnspython")
    print("-" * 70)
    print("方法3: 制限を回避して現在の環境に直接 pip インストールする場合 (※要リスク理解)")
    print("    pip install dnspython --break-system-packages")
    print("=" * 70)
    sys.exit(1)


def check_single_target(domain, rdtype, expected, dns_server=None):
    """単一のドメイン・レコードタイプを検証する関数"""
    if isinstance(expected, str):
        expected_list = [expected]
    else:
        expected_list = expected

    # カスタムDNSリゾルバーの設定
    resolver = dns.resolver.Resolver()
    if dns_server:
        resolver.nameservers = [dns_server]
        print(f"Checking: {domain} ({rdtype}) using DNS [{dns_server}]...")
    else:
        print(f"Checking: {domain} ({rdtype}) using System Default DNS...")

    try:
        answers = resolver.resolve(domain, rdtype)
        actual_values = []
        for rdata in answers:
            if rdtype == "TXT":
                txt_value = "".join([s.decode('utf-8') for s in rdata.strings])
                actual_values.append(txt_value)
            else:
                actual_values.append(str(rdata))

        # 表記ゆれの考慮
        clean_actual = {v.rstrip('.').strip('"') for v in actual_values}
        clean_expected = {v.rstrip('.').strip('"') for v in expected_list}

        # 判定
        if clean_expected.issubset(clean_actual):
            print(f"  => {COLOR_GREEN}[OK]{COLOR_RESET} 期待値が含まれています。 (検出: {actual_values})")
            print("-" * 40)
            return True
        else:
            print(f"  => {COLOR_RED}[NG]{COLOR_RESET} 一致しませんでした。")
            print(f"     期待値: {expected_list}")
            print(f"     実際の値: {actual_values}")
            print("-" * 40)
            return False

    except dns.resolver.NoAnswer:
        print(f"  => {COLOR_RED}[NG]{COLOR_RESET} 指定されたタイプ ({rdtype}) のレコードが見つかりません。")
    except dns.resolver.NXDOMAIN:
        print(f"  => {COLOR_RED}[NG]{COLOR_RESET} ドメインが存在しません。")
    except Exception as e:
        print(f"  => {COLOR_RED}[ERROR]{COLOR_RESET} エラーが発生しました: {e}")
        
    print("-" * 40)
    return False


def main():
    parser = argparse.ArgumentParser(description="DNS Name Resolution Checker")
    parser.add_argument("--domain", help="チェックしたいドメイン名")
    parser.add_argument("--type", help="レコードタイプ (A, AAAA, TXT, NS, CNAMEなど)")
    parser.add_argument("--value", "--expectedvalue", help="期待する値")
    parser.add_argument("--dns", help="一時的に使用するDNSサーバーのIPアドレス (例: 8.8.8.8)")
    parser.add_argument("--file", default="check-domain.json", help="読み込むJSONファイルパス (デフォルト: check-domain.json)")
    
    args = parser.parse_args()

    # CLI引数が指定された場合
    if args.domain:
        if not args.type or not args.value:
            parser.error("--domain を指定する場合は、--type と --value（または --expectedvalue）も必須です。")
        
        success = check_single_target(args.domain, args.type.upper(), args.value, dns_server=args.dns)
        sys.exit(0 if success else 1)
    
    # 引数がない場合はJSONファイルから一括チェック
    else:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                targets = json.load(f)
            for target in targets:
                check_single_target(
                    target.get("domain"), 
                    target.get("type"), 
                    target.get("expectedvalue"),
                    dns_server=args.dns
                )
        except FileNotFoundError:
            print(f"{COLOR_RED}[ERROR]{COLOR_RESET} JSONファイル '{args.file}' が見つかりません。")
            sys.exit(1)


if __name__ == "__main__":
    main()