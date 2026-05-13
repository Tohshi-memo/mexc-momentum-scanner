# Decision Report

- generated_at: 2026-05-13T06:03:07.994670+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4190**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.92% / filled 20/20。**
- 全期間 MARKET基準: n=4190, expectancy=-0.12%
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
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.36% | **+0.21%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.28% | **+0.17%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.17** / 初期 $100.00 (+20.17%)
- 確定: 326件 (Win 92 / Loss 116 / Flat 118) / skip 425件
- 成長率目線: 平均log +0.000564 / 幾何平均 +0.056% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.14% 残高後 $120.17

## 4. Latest Market Context

- 更新: 2026-05-13T06:03:04.791610+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80955.3
- Funnel: target 765 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +37.28% | $4,161,164.90 |
| SATO/USDT:USDT | +26.00% | $1,214,981.69 |
| GUA/USDT:USDT | +23.66% | $3,902,487.25 |
| LAB/USDT:USDT | +20.93% | $105,148,219.13 |
| PEAQ/USDT:USDT | +14.17% | $2,557,745.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +0.99% | +1.02% |
| UB/USDT:USDT | below_1h_threshold | +0.83% | +0.87% |
| RIVER/USDT:USDT | below_1h_threshold | +0.75% | +0.79% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +0.32% | +0.36% |
| GUA/USDT:USDT | below_1h_threshold | +0.23% | +0.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
