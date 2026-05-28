# Decision Report

- generated_at: 2026-05-28T21:10:06.373975+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4993**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4993, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.50% | **+0.88%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.80% | **+0.81%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.36% | **+0.54%** |
| MARKET_LONG | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 726件 (Win 175 / Loss 222 / Flat 329) / skip 828件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ETHFI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-28T21:10:03.983890+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=73617.8
- Funnel: target 772 → liquid 163 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +35.33% | $11,850,330.05 |
| CLO/USDT:USDT | +24.71% | $1,107,612.46 |
| DELLSTOCK/USDT:USDT | +19.80% | $5,119,298.02 |
| VVV/USDT:USDT | +11.38% | $10,250,195.14 |
| XPL/USDT:USDT | +10.78% | $3,908,629.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +2.11% | +2.02% |
| SWARMS/USDT:USDT | below_1h_threshold | +1.70% | +1.61% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.48% | +1.39% |
| XLM/USDT:USDT | below_1h_threshold | +1.24% | +1.15% |
| BSB/USDT:USDT | below_1h_threshold | +1.21% | +1.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
