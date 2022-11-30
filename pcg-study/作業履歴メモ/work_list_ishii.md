2020/10/11

やったこと
	1.RDSの構築
	2.pgAdminからの接続

1．RDSの構築
	サブネットグループの作成（作業PCからアクセスできるよう、パブリックサブネットを利用）
	セキュリティグループの作成（5432ポートからの任意のIPからのアクセスを許可）
	RDSの作成（詳細はRDSパラメータ.pngに記載）

2．pgAdminからの接続
	https://docs.aws.amazon.com/ja_jp/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html
	『トピック：PostgreSQL DB インスタンスに接続する』を参照
	接続のパラメータ
	  hostname/address : 
		pcg-postgre-1.co1gpyhjneej.ap-northeast-1.rds.amazonaws.com
	　Port : 
	 	5432
	　Maintenance database : （規定値でこれみたいですね、てっきりこちらで命名したものかと思ってました）
	 	postgres
	  Username : 
	  	postgrte_admin
	  Password : （置く場所が迷子にならないよう暫定的においています）
	  	sugoizo-postgre%555
	
上記手順でDBに接続できることを確認した



2021/01/10
前提

    EC2 → Amazon Linux 2

    IAMロール → EC2には付与されていない

手順の流れ

1. IAMロールの設定
2. Cloudwatch agentのインストール
3. 設定ファイルの作成
4. Cloudwatch agentの起動
5. Cloudwatchコンソールで確認

手順

1.IAMロールの設定

    ①AWSコンソールにログインし、「サービス ＞IAM ＞ロール ＞ ロール作成」 を開く

    ②以下の選択して、「次のステップ：アクセス権限」を押下

        信頼されたエンティティの種類：AWSのサービス

        ユースケース：EC2

    ③以下のポリシーをチェックをつけ、「次のステップ：タグ」を押下

        IAMポリシー：CloudWatchAgentAdminPolicy

    ④タグは入力せず（必要に応じて入力してもOK）「次のステップ：確認」を押下

    ⑤以下のロール名を入力し、「ロールの作成」を押下（IAMロール作成完了）

        ロール名：ec2_cloudwatch_agent_role

    ⑥「サービス ＞EC2 ＞インスタンス」を開く

    ⑦対象インスタンスを選択し、「アクション ＞セキュリティ ＞IAMロールを変更」を開く

    ⑧以下のIAMロールを入力し、「保存」を押下（IAMロールアタッチ完了）

        IAMロール：ec2_cloudwatch_agent_role
※1つのインスタンスに複数個のIAMロールをアタッチできないため、複数のIAM
IAMポリシーを含んだ（例えば、CloudwatchとS3など）EC2用のIAMロールを作成する必要がある。

IAMロールの作成：[https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent.html](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/create-iam-roles-for-cloudwatch-agent.html)

2.Cloudwatch agentのインストール

    ①Teratermを使用して、対象インスタンスへSSH接続をする

    ②以下のコマンドを実行し、Cloudwatch agentをインストールする

```bash
  $ sudo yum install amazon-cloudwatch-agent 
```

エージェントのインストール：[https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html)   

    ③以下のコマンドを実行し、インストールが成功したかを確認する

```bash
$ systemctl list-unit-files --type=service
  #サービス名は、「amazon-cloudwatch-agent.service」
```

3.設定ファイルの作成

    ①以下のコマンドを入力して、amazon-cloudwatch-agent.jsonを作成する

```bash
$ sudo vi /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
```

    amazon-cloudwatch-agent.json

```json
{
      "agent": {
        "metrics_collection_interval": 60,
        "logfile": "/opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log"
      },
      "metrics": {
        "namespace": "CWAgent",
        "metrics_collected": {
          "mem": {
            "measurement": [
              "mem_used",
              "mem_cached",
              "mem_total",
              "mem_used_percent"
            ],
            "metrics_collection_interval": 60
          },
          "processes": {
            "measurement": [
              "processes_running",
              "processes_sleeping",
              "processes_dead"
            ],
            "metrics_collection_interval": 60
          }
        },
        "append_dimensions": {
          "ImageId": "${aws:ImageId}",
          "InstanceId": "${aws:InstanceId}",
          "InstanceType": "${aws:InstanceType}"
        }
      },
      "logs": {
        "logs_collected": {
          "files": {
            "collect_list": [
              {
                "file_path": "/opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log",
                "log_group_name": "pcg_EC2",
                "log_stream_name": "{hostname}.log",
                  "timestamp_format": "%H: %M: %S%y%b%-d",
                "timezone": "Local"
              },
              {
                "file_path": "/opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log",
                "log_group_name": "pcg_EC2",
                "log_stream_name": "{hostname}.log",
                "timezone": "Local"
              }
            ]
          }
        },
        "log_stream_name": "PCG_LOG"
      }
    }
```

設定ファイルの詳細：[https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-Configuration-File-Details.html)

標準で取得しているメトリクス：[https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/monitoring_ec2.html](https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/monitoring_ec2.html)ファイル

設定できるカスタムメトリクス：[https://www.notion.so/Cloudwatch-agent-df22d25da4a94f24b0430bd350a359f0#00b401d9173c48a985e178f75ea042dd](https://www.notion.so/Cloudwatch-agent-df22d25da4a94f24b0430bd350a359f0#00b401d9173c48a985e178f75ea042dd)

    ②以下のコマンドを実行し、jsonファイルのパーミッションを変更する

```bash
$ sudo chmod 755 /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
```

※ 実行ユーザーにrxの権限を付与する必要がある

    ③以下のコマンドを実行し、ファイルを確認する

```bash
$ ls -l /opt/aws/amazon-cloudwatch-agent/etc/
```

4.Cloudwatch agentの起動

    ①以下のコマンドを実行し、Cloudwatch agentを起動する

```bash
$ sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
```

※コマンドを実行すると、Jsonファイルがなくなりtomlファイルが生成される

エージェントの起動：[https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-common-scenarios.html](https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-common-scenarios.html)

    ②以下のコマンドを実行し、起動を確認する

```bash
$ systemctl status amazon-cloudwatch-agent.service
```

5.Cloudwatchコンソールで確認

    ①AWSコンソールにログインし、「サービス ＞Cloudwatch ＞メトリクス」 を開く

    ②カスタム名前空間の「CWAgent」を開き、メトリクスが取得できたことを確認すrつ

