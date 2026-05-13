# Decision Report

- generated_at: 2026-05-13T07:03:05.867711+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4193**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.79% / filled 20/20。**
- 全期間 MARKET基準: n=4193, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.79% | **+1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +2.10% | **+1.89%** |
| ASK | 20/20 | 100.0% | +1.80% | **+1.80%** |
| MARKET | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.71% | **+1.11%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.28% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.74% | **+0.37%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.22% | **-0.02%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | -0.27% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.57** / 初期 $100.00 (+19.57%)
- 確定: 329件 (Win 92 / Loss 117 / Flat 120) / skip 425件
- 成長率目線: 平均log +0.000543 / 幾何平均 +0.054% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $119.57

## 4. Latest Market Context

- 更新: 2026-05-13T07:03:02.494859+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80976.1
- Funnel: target 765 → liquid 188 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +33.84% | $5,378,855.48 |
| SATO/USDT:USDT | +21.88% | $1,239,733.65 |
| LAB/USDT:USDT | +18.94% | $104,166,837.98 |
| PEAQ/USDT:USDT | +17.03% | $2,597,464.61 |
| INJ/USDT:USDT | +14.18% | $57,048,783.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +0.78% | +0.74% |
| INJ/USDT:USDT | below_1h_threshold | +0.74% | +0.70% |
| UB/USDT:USDT | below_1h_threshold | +0.66% | +0.62% |
| RIVER/USDT:USDT | below_1h_threshold | +0.57% | +0.53% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.46% | +0.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
