# Decision Report

- generated_at: 2026-05-21T14:34:04.473958+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4640**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4640, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.81% | **-0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.81% | **+0.61%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.89% | **+1.13%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.31% | **+1.04%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.56% | **+0.78%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 655件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T14:34:01.562628+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77068.7
- Funnel: target 766 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +54.91% | $15,062,689.37 |
| NEX/USDT:USDT | +47.07% | $1,506,748.69 |
| EDEN/USDT:USDT | +43.90% | $34,118,313.24 |
| ROAM/USDT:USDT | +42.49% | $2,331,696.15 |
| PROVE/USDT:USDT | +37.55% | $6,649,450.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HYPE/USDT:USDT | below_1h_threshold | +4.09% | +4.12% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.88% | +2.91% |
| EDEN/USDT:USDT | below_1h_threshold | +2.66% | +2.69% |
| ROAM/USDT:USDT | below_1h_threshold | +2.37% | +2.40% |
| NEX/USDT:USDT | below_1h_threshold | +2.35% | +2.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
