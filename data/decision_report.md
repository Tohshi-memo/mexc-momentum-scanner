# Decision Report

- generated_at: 2026-06-04T05:56:47.732069+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5607**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.81% / filled 20/20。**
- 全期間 MARKET基準: n=5607, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.81% | **+2.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.92% | **+2.92%** |
| MARKET | 20/20 | 100.0% | +2.81% | **+2.81%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.29% | **+0.97%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | -0.01% | **-0.01%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.23% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$99.04** / 初期 $100.00 (-0.96%)
- 確定トレード: 94件 (TP 29 / SL 62 / EXP 3)
- 最新: ICP/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.04
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1005件 (Win 239 / Loss 312 / Flat 454) / skip 1163件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LIT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T05:56:43.863610+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.66% price=63947.8
- Funnel: target 771 → liquid 167 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.4 >= 65=1, 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +47.16% | $1,445,295.69 |
| EPIC/USDT:USDT | +23.99% | $4,651,858.98 |
| SIREN/USDT:USDT | +19.45% | $1,562,926.85 |
| OPN/USDT:USDT | +16.59% | $29,145,183.82 |
| BP/USDT:USDT | +11.84% | $1,883,894.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +1.94% | +2.59% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.47% | +2.12% |
| BEAT/USDT:USDT | below_1h_threshold | +1.16% | +1.81% |
| ZEC/USDT:USDT | below_1h_threshold | +1.11% | +1.76% |
| LAB/USDT:USDT | below_1h_threshold | +0.54% | +1.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
