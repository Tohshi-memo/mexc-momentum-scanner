# Decision Report

- generated_at: 2026-05-12T15:16:14.842409+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4135**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.83% / filled 20/20。**
- 全期間 MARKET基準: n=4135, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.85% | **+0.85%** |
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.36% | **+0.23%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | -0.03% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$115.92** / 初期 $100.00 (+15.92%)
- 確定: 271件 (Win 74 / Loss 94 / Flat 103) / skip 425件
- 成長率目線: 平均log +0.000545 / 幾何平均 +0.055% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEAQ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $115.92

## 4. Latest Market Context

- 更新: 2026-05-12T15:16:11.420257+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80531.2
- Funnel: target 763 → liquid 194 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +93.69% | $29,890,492.86 |
| GIGA/USDT:USDT | +57.49% | $7,848,333.23 |
| SKYAI/USDT:USDT | +39.57% | $39,015,261.67 |
| USELESS/USDT:USDT | +36.86% | $11,340,413.64 |
| GUA/USDT:USDT | +34.66% | $3,803,660.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +4.95% | +4.92% |
| H/USDT:USDT | below_1h_threshold | +3.80% | +3.78% |
| USELESS/USDT:USDT | below_1h_threshold | +3.30% | +3.28% |
| DYM/USDT:USDT | below_1h_threshold | +2.97% | +2.94% |
| VVV/USDT:USDT | below_1h_threshold | +1.80% | +1.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
