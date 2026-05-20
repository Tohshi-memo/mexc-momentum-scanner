# Decision Report

- generated_at: 2026-05-20T21:09:12.272360+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4580**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4580, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.50% | **-0.60%** |
| LIMIT_9PCT | 6/20 | 30.0% | -2.00% | **-0.60%** |
| LIMIT_10PCT | 6/20 | 30.0% | -2.00% | **-0.60%** |
| LIMIT_5PCT | 11/20 | 55.0% | -1.11% | **-0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/11 | 63.6% | +3.36% | **+2.14%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.35% | **+2.12%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.87% | **+1.72%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.02% | **+1.52%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.11** / 初期 $100.00 (+25.11%)
- 確定: 539件 (Win 138 / Loss 179 / Flat 222) / skip 602件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $125.11

## 4. Latest Market Context

- 更新: 2026-05-20T21:09:10.203777+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77688.5
- Funnel: target 758 → liquid 122 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +35.66% | $27,080,703.57 |
| FIDA/USDT:USDT | +29.55% | $10,032,036.58 |
| NIL/USDT:USDT | +18.83% | $2,443,177.20 |
| JTO/USDT:USDT | +13.39% | $2,041,177.88 |
| BEAT/USDT:USDT | +10.47% | $1,709,303.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.12% | +3.11% |
| BSB/USDT:USDT | below_1h_threshold | +2.99% | +2.98% |
| FIDA/USDT:USDT | below_1h_threshold | +1.60% | +1.59% |
| EDEN/USDT:USDT | below_1h_threshold | +0.79% | +0.79% |
| RIVER/USDT:USDT | below_1h_threshold | +0.60% | +0.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
