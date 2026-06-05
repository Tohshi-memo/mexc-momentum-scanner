# Decision Report

- generated_at: 2026-06-05T16:11:24.243520+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5728**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=5728, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.63% | **+2.63%** |
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.90% | **+1.81%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.89% | **+1.51%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.77% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.63% | **+0.47%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.74% | **+0.37%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.29% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1010件 (Win 239 / Loss 313 / Flat 458) / skip 1279件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OPN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T16:11:21.676556+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.76% price=59946.0
- Funnel: target 773 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +3.44% | $2,782,751.19 |
| HOME/USDT:USDT | +3.13% | $8,624,646.18 |
| BSB/USDT:USDT | +3.08% | $3,660,023.69 |
| UP/USDT:USDT | +1.86% | $2,794,610.59 |
| GUA/USDT:USDT | +1.49% | $1,963,305.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +3.58% | +4.35% |
| BSB/USDT:USDT | below_1h_threshold | +3.09% | +3.85% |
| HOME/USDT:USDT | below_1h_threshold | +3.06% | +3.82% |
| UP/USDT:USDT | below_1h_threshold | +1.86% | +2.62% |
| GUA/USDT:USDT | below_1h_threshold | +1.49% | +2.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
