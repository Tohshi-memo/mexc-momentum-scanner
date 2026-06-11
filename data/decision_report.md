# Decision Report

- generated_at: 2026-06-11T23:58:57.717349+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6425**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=6425, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/18 | 16.7% | +3.69% | **+0.61%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.55% | **+0.50%** |
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |
| ASK | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |
| ASK_LONG | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | -0.06% | **-0.03%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.29% | **-0.13%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | -0.58% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$94.70** / 初期 $100.00 (-5.30%)
- 確定トレード: 15件 (TP 1 / SL 13 / EXP 1)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.46% 残高後 $94.70
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1659件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-11T23:58:55.046770+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=63581.9
- Funnel: target 782 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +81.73% | $24,121,598.43 |
| VELVET/USDT:USDT | +80.61% | $130,531,900.07 |
| STG/USDT:USDT | +28.07% | $14,189,796.12 |
| NAORIS/USDT:USDT | +18.47% | $1,463,191.59 |
| UB/USDT:USDT | +17.86% | $1,852,917.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +4.20% | +4.02% |
| H/USDT:USDT | below_1h_threshold | +3.96% | +3.78% |
| FHE/USDT:USDT | below_1h_threshold | +2.31% | +2.13% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.86% | +1.68% |
| XMR/USDT:USDT | below_1h_threshold | +1.72% | +1.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
