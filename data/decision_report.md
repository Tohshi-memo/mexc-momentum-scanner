# Decision Report

- generated_at: 2026-05-20T10:08:41.194240+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4538**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4538, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.73% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.14% | **-0.11%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.73% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.59%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.44% | **+0.29%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.97% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.64** / 初期 $100.00 (+25.64%)
- 確定: 500件 (Win 131 / Loss 171 / Flat 198) / skip 599件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $125.64

## 4. Latest Market Context

- 更新: 2026-05-20T10:08:39.123114+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=77539.7
- Funnel: target 762 → liquid 133 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +104.16% | $1,639,230.46 |
| PROMPT/USDT:USDT | +32.06% | $12,572,897.10 |
| FIDA/USDT:USDT | +29.35% | $2,815,929.88 |
| EDEN/USDT:USDT | +25.53% | $22,006,245.51 |
| LIT/USDT:USDT | +23.30% | $8,798,696.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_1h_threshold | +3.81% | +3.70% |
| FOGO/USDT:USDT | below_1h_threshold | +3.10% | +2.99% |
| BSB/USDT:USDT | below_1h_threshold | +2.96% | +2.85% |
| DASH/USDT:USDT | below_1h_threshold | +1.24% | +1.12% |
| SATO/USDT:USDT | below_1h_threshold | +0.87% | +0.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
