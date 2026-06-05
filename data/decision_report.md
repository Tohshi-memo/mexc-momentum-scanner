# Decision Report

- generated_at: 2026-06-05T17:21:48.951440+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5734**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=5734, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.62% | **+1.46%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.13% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | -0.17% | **-0.06%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.46% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1011件 (Win 239 / Loss 313 / Flat 459) / skip 1284件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T17:21:43.588841+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.87% price=60829.1
- Funnel: target 773 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +17.09% | $2,921,812.70 |
| GUA/USDT:USDT | +10.79% | $1,833,772.72 |
| HOME/USDT:USDT | +8.15% | $8,127,750.45 |
| ENA/USDT:USDT | +8.09% | $49,040,792.59 |
| LAB/USDT:USDT | +5.52% | $100,446,048.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.88% | +5.74% |
| EPIC/USDT:USDT | below_1h_threshold | +3.15% | +4.02% |
| HEI/USDT:USDT | below_1h_threshold | +1.41% | +2.28% |
| ENA/USDT:USDT | below_1h_threshold | +0.92% | +1.79% |
| XLM/USDT:USDT | below_1h_threshold | +0.53% | +1.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
