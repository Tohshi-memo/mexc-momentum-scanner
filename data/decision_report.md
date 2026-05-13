# Decision Report

- generated_at: 2026-05-13T06:22:59.282182+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4191**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=4191, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.25% | **+1.12%** |
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| MARKET | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.26% | **+0.89%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.78% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.36% | **+0.21%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | -0.04% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.57** / 初期 $100.00 (+19.57%)
- 確定: 327件 (Win 92 / Loss 117 / Flat 118) / skip 425件
- 成長率目線: 平均log +0.000546 / 幾何平均 +0.055% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TROLLSOL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $119.57

## 4. Latest Market Context

- 更新: 2026-05-13T06:22:55.862403+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=81021.9
- Funnel: target 765 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +39.77% | $4,515,111.46 |
| SATO/USDT:USDT | +25.39% | $1,226,381.21 |
| GUA/USDT:USDT | +22.23% | $4,057,390.74 |
| LAB/USDT:USDT | +20.25% | $106,521,094.86 |
| PEAQ/USDT:USDT | +14.03% | $2,567,590.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +1.77% | +1.72% |
| BASED/USDT:USDT | below_1h_threshold | +1.20% | +1.15% |
| S/USDT:USDT | below_1h_threshold | +1.04% | +0.99% |
| XPL/USDT:USDT | below_1h_threshold | +1.01% | +0.96% |
| CFX/USDT:USDT | below_1h_threshold | +1.00% | +0.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
