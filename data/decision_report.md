# Decision Report

- generated_at: 2026-05-12T01:48:03.343233+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4086**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4086, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.82% | **+0.62%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.74% | **+0.51%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.64% | **+0.51%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.46% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.97% | **+0.68%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.42** / 初期 $100.00 (+8.42%)
- 確定: 223件 (Win 56 / Loss 78 / Flat 89) / skip 424件
- 成長率目線: 平均log +0.000363 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $108.42

## 4. Latest Market Context

- 更新: 2026-05-12T01:47:59.417994+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.58% price=81036.6
- Funnel: target 762 → liquid 189 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.1 >= 65=1, 4h RSI 81.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +37.25% | $1,330,655.90 |
| USELESS/USDT:USDT | +19.07% | $3,939,274.03 |
| SAGA/USDT:USDT | +18.62% | $7,197,383.25 |
| SKYAI/USDT:USDT | +18.53% | $37,922,550.39 |
| H/USDT:USDT | +16.63% | $15,763,216.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.81% | +4.39% |
| LAB/USDT:USDT | below_1h_threshold | +3.61% | +4.19% |
| USELESS/USDT:USDT | below_1h_threshold | +2.46% | +3.04% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.78% | +2.36% |
| ZBT/USDT:USDT | below_1h_threshold | +1.75% | +2.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
