# Decision Report

- generated_at: 2026-06-11T21:07:43.198970+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6408**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.00% / filled 20/20。**
- 全期間 MARKET基準: n=6408, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+2.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.00% | **+2.00%** |
| ASK | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.18% | **+1.01%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.18% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.01% | **+0.50%** |
| ASK_LONG | 20/20 | 100.0% | +0.04% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.48** / 初期 $100.00 (+51.48%)
- 確定: 1325件 (Win 344 / Loss 426 / Flat 555) / skip 1644件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NAORIS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.25% 残高後 $151.48

## 4. Latest Market Context

- 更新: 2026-06-11T21:07:39.968243+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=63430.4
- Funnel: target 782 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +81.70% | $118,488,016.56 |
| ESPORTS/USDT:USDT | +49.37% | $14,809,857.34 |
| NAORIS/USDT:USDT | +15.96% | $1,480,061.92 |
| UB/USDT:USDT | +13.35% | $1,676,861.18 |
| XPL/USDT:USDT | +10.98% | $1,577,108.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EIGEN/USDT:USDT | below_1h_threshold | +2.68% | +2.57% |
| RENDER/USDT:USDT | below_1h_threshold | +1.47% | +1.36% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.35% | +1.24% |
| BEAT/USDT:USDT | below_1h_threshold | +1.34% | +1.23% |
| XPL/USDT:USDT | below_1h_threshold | +1.26% | +1.15% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
