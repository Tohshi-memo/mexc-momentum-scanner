# Decision Report

- generated_at: 2026-05-13T09:18:02.364392+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4206**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4206, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| ASK | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.22% | **+0.21%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.85% | **+0.64%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.63% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.78** / 初期 $100.00 (+19.78%)
- 確定: 341件 (Win 94 / Loss 124 / Flat 123) / skip 426件
- 成長率目線: 平均log +0.000529 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $119.78

## 4. Latest Market Context

- 更新: 2026-05-13T09:17:59.320616+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=81188.2
- Funnel: target 765 → liquid 187 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +40.87% | $1,566,980.16 |
| UB/USDT:USDT | +28.14% | $5,581,076.65 |
| LAB/USDT:USDT | +27.23% | $108,527,758.01 |
| SATO/USDT:USDT | +26.12% | $1,303,652.25 |
| INJ/USDT:USDT | +22.01% | $75,165,008.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INJ/USDT:USDT | below_1h_threshold | +3.96% | +3.92% |
| UB/USDT:USDT | below_1h_threshold | +3.66% | +3.63% |
| BILL/USDT:USDT | below_1h_threshold | +3.63% | +3.60% |
| SATO/USDT:USDT | below_1h_threshold | +3.00% | +2.97% |
| TIA/USDT:USDT | below_1h_threshold | +2.13% | +2.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
