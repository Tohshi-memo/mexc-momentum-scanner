# Decision Report

- generated_at: 2026-06-11T21:19:42.673710+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6409**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.03% / filled 20/20。**
- 全期間 MARKET基準: n=6409, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+2.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.03% | **+2.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.03% | **+2.03%** |
| ASK | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.28% | **+1.08%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.52% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.01% | **+0.50%** |
| ASK_LONG | 20/20 | 100.0% | -0.20% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.48** / 初期 $100.00 (+51.48%)
- 確定: 1326件 (Win 344 / Loss 426 / Flat 556) / skip 1644件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XPL/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $151.48

## 4. Latest Market Context

- 更新: 2026-06-11T21:19:39.888472+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=63485.9
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +88.04% | $120,130,716.07 |
| ESPORTS/USDT:USDT | +52.98% | $15,038,169.72 |
| NAORIS/USDT:USDT | +16.43% | $1,496,421.01 |
| UB/USDT:USDT | +13.81% | $1,694,504.44 |
| STG/USDT:USDT | +12.95% | $12,473,116.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.35% | +3.15% |
| NEAR/USDT:USDT | below_1h_threshold | +2.94% | +2.74% |
| EIGEN/USDT:USDT | below_1h_threshold | +2.73% | +2.53% |
| XPL/USDT:USDT | below_1h_threshold | +2.62% | +2.42% |
| RENDER/USDT:USDT | below_1h_threshold | +2.02% | +1.82% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
