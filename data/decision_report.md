# Decision Report

- generated_at: 2026-05-07T16:07:48.790653+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3654**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.26% / filled 20/20。**
- 全期間 MARKET基準: n=3654, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.26% | **+0.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.98% | **+1.19%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.75% | **+0.72%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.72% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.86% | **+2.00%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +2.72% | **+1.49%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.62% | **+1.44%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +1.46% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$112.16** / 初期 $100.00 (+12.16%)
- 確定: 148件 (Win 46 / Loss 53 / Flat 49) / skip 67件
- 成長率目線: 平均log +0.000775 / 幾何平均 +0.078% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $112.16

## 4. Latest Market Context

- 更新: 2026-05-07T16:07:37.858640+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=79729.6
- Funnel: target 771 → liquid 178 → pre 50 → checked 50 → surge 5 → strict 4
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +11.04% | $4,047,026.32 |
| FHE/USDT:USDT | +7.74% | $13,545,181.71 |
| PENGUIN/USDT:USDT | +7.35% | $4,583,712.38 |
| BILL/USDT:USDT | +6.34% | $10,939,692.00 |
| LAB/USDT:USDT | +6.08% | $263,383,561.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.30% | +2.47% |
| STRK/USDT:USDT | below_1h_threshold | +1.72% | +1.88% |
| DASH/USDT:USDT | below_1h_threshold | +1.42% | +1.59% |
| NIL/USDT:USDT | below_1h_threshold | +1.40% | +1.57% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.31% | +1.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
