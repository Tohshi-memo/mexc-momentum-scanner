# Decision Report

- generated_at: 2026-05-07T07:07:38.067977+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3584**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=3584, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.01% | **+0.91%** |
| ASK | 20/20 | 100.0% | +0.72% | **+0.72%** |
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.63% | **+1.18%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.54% | **+0.85%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.77% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.15** / 初期 $100.00 (+6.15%)
- 確定: 78件 (Win 28 / Loss 32 / Flat 18) / skip 67件
- 成長率目線: 平均log +0.000765 / 幾何平均 +0.077% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.15

## 4. Latest Market Context

- 更新: 2026-05-07T07:07:34.693133+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=81401.7
- Funnel: target 771 → liquid 187 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1, 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +246.10% | $1,882,745.84 |
| B3/USDT:USDT | +80.10% | $9,830,117.73 |
| DOGS/USDT:USDT | +71.73% | $12,609,630.78 |
| PENGUIN/USDT:USDT | +69.23% | $1,482,547.34 |
| EVAA/USDT:USDT | +52.89% | $1,291,186.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +4.88% | +4.88% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.13% | +2.12% |
| B/USDT:USDT | below_1h_threshold | +1.36% | +1.35% |
| FET/USDT:USDT | below_1h_threshold | +1.23% | +1.23% |
| BRETT/USDT:USDT | below_1h_threshold | +0.94% | +0.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
