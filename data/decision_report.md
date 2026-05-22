# Decision Report

- generated_at: 2026-05-22T17:04:40.666309+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4721**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4721, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.73% | **+1.13%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.90% | **+0.81%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.84% | **+0.75%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.98% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.34% | **+0.74%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.66% | **+0.29%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.30% | **+0.23%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.89% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.82** / 初期 $100.00 (+21.82%)
- 確定: 567件 (Win 145 / Loss 187 / Flat 235) / skip 715件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $121.82

## 4. Latest Market Context

- 更新: 2026-05-22T17:04:38.556821+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=76944.4
- Funnel: target 768 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +25.14% | $25,959,497.49 |
| GENIUS/USDT:USDT | +6.91% | $5,380,811.35 |
| BEAT/USDT:USDT | +6.00% | $31,637,829.91 |
| GUA/USDT:USDT | +3.71% | $1,034,547.87 |
| USELESS/USDT:USDT | +3.24% | $1,146,576.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEX/USDT:USDT | below_1h_threshold | +1.10% | +1.06% |
| GENIUS/USDT:USDT | below_1h_threshold | +1.09% | +1.05% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.67% | +0.63% |
| PLUME/USDT:USDT | below_1h_threshold | +0.66% | +0.62% |
| GRASS/USDT:USDT | below_1h_threshold | +0.65% | +0.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
