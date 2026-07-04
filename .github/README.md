# [dns_domain_check](https://github.com/n138-kz/dns_domain_check)

## Repos Info

<div align="center">

  [![GitHub repo license](https://img.shields.io/github/license/n138-kz/dns_domain_check)](/LICENSE)
  [![GitHub top language](https://img.shields.io/github/languages/top/n138-kz/dns_domain_check)](/../../)
  [![GitHub repo size](https://img.shields.io/github/repo-size/n138-kz/dns_domain_check)](/../../)
  [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/n138-kz/dns_domain_check)](/../../)

</div>
<div align="center">

  [![GitHub last commit](https://img.shields.io/github/last-commit/n138-kz/dns_domain_check)](/../../commits)
  [![GitHub commit activity](https://img.shields.io/github/commit-activity/w/n138-kz/dns_domain_check)](/../../commits)
  [![GitHub commit activity](https://img.shields.io/github/commit-activity/t/n138-kz/dns_domain_check)](/../../commits)
  [![GitHub language count](https://img.shields.io/github/languages/count/n138-kz/dns_domain_check)](/../../)

</div>
<div align="center">

  [![GitHub issues](https://img.shields.io/github/issues/n138-kz/dns_domain_check)](/../../issues)
  [![GitHub issues closed](https://img.shields.io/github/issues-closed/n138-kz/dns_domain_check)](/../../issues)
  [![GitHub pull requests](https://img.shields.io/github/issues-pr/n138-kz/dns_domain_check)](/../../pulls)
  [![GitHub pull requests closed](https://img.shields.io/github/issues-pr-closed/n138-kz/dns_domain_check)](/../../pulls)

</div>
<div align="center">

  [![](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/channel/UCOX8Iv1r0V18lbOnohE7lWQ)
  [![](https://img.shields.io/badge/Twitch-6441A5?style=for-the-badge&logo=twitch&logoColor=white)](https://www.twitch.tv/yuukomiya)
  [![](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/n138kz)
  <br>
  [![](https://img.shields.io/youtube/channel/subscribers/UCOX8Iv1r0V18lbOnohE7lWQ)](https://youtube.com/channel/UCOX8Iv1r0V18lbOnohE7lWQ)
  [![](https://img.shields.io/twitch/status/YuuKomiya)](https://www.twitch.tv/yuukomiya)

</div>

## Refs

- [![](https://www.google.com/s2/favicons?size=64&domain=https://github.com)dns_domain_check](https://github.com/n138-kz/dns_domain_check/)

## How to use

- Python version: 3.7 or over

1. 依存ライブラリをインストールする
    ```sh
    python3 -m pip install -r requirements.txt
    ```
2. JSONファイルを作成する
    ファイル名: `check-domain.json`  
    内容:   
    ```json
    [
      {
        "domain": "dns.google",
        "type": "A",
        "expectedvalue": "8.8.8.8"
      }
    ]
    ```
3. python3 コマンド経由でスクリプトを実行する。
    ```sh
    python3 dns_check.py
    ```

---


1. 依存ライブラリをインストールする
    ```sh
    python3 -m pip install -r requirements.txt
    ```
2. python3 コマンド経由でスクリプトを実行する。
    ```sh
    python3 dns_check.py --domain dns.google --type a --value 8.8.8.8
    ```

    実行結果例:
    ```sh
    > python3 dns_check.py --domain dns.google --type a --value 8.8.8.8
    Checking: dns.google (A) using System Default DNS...
      => [OK] 期待値が含まれています。 (検出: ['8.8.4.4', '8.8.8.8'])
----------------------------------------
  ```

## License

[Copyright (c) 2026 Yuu Komiya (n138), Under MIT License](LICENSE)  
