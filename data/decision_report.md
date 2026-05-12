# Decision Report

- generated_at: 2026-05-12T15:23:00.552487+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4137**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.83% / filled 20/20。**
- 全期間 MARKET基準: n=4137, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.03% | **+1.03%** |
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | -0.28% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$116.06** / 初期 $100.00 (+16.06%)
- 確定: 273件 (Win 75 / Loss 95 / Flat 103) / skip 425件
- 成長率目線: 平均log +0.000546 / 幾何平均 +0.055% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $116.06

## 4. Latest Market Context

- 更新: 2026-05-12T15:22:56.459587+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=80395.5
- Funnel: target 763 → liquid 194 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.9 >= 65=1, 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +102.65% | $31,577,862.09 |
| GIGA/USDT:USDT | +54.56% | $7,904,283.03 |
| SKYAI/USDT:USDT | +38.22% | $39,633,881.60 |
| USELESS/USDT:USDT | +36.91% | $11,409,505.20 |
| GUA/USDT:USDT | +34.86% | $3,827,279.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOLV/USDT:USDT | below_1h_threshold | +4.54% | +4.69% |
| DYM/USDT:USDT | below_1h_threshold | +4.29% | +4.43% |
| H/USDT:USDT | below_1h_threshold | +3.97% | +4.12% |
| USELESS/USDT:USDT | below_1h_threshold | +3.34% | +3.48% |
| BASED/USDT:USDT | below_1h_threshold | +1.82% | +1.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
