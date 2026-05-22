# Decision Report

- generated_at: 2026-05-22T07:03:56.973667+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4673**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.69% / filled 20/20。**
- 全期間 MARKET基準: n=4673, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| ASK | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| MARKET | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.88% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +4.13% | **+2.29%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.42% | **+1.21%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.13% | **+0.74%** |
| ASK_LONG | 20/20 | 100.0% | +0.56% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 686件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T07:03:54.913805+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=77290.6
- Funnel: target 768 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +64.61% | $2,694,500.80 |
| NEAR/USDT:USDT | +21.37% | $73,850,053.37 |
| GRASS/USDT:USDT | +20.54% | $4,513,101.37 |
| PLUME/USDT:USDT | +12.17% | $1,830,961.53 |
| EDEN/USDT:USDT | +10.90% | $19,383,831.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +0.03% | +0.15% |
| PENDLE/USDT:USDT | below_1h_threshold | +0.01% | +0.13% |
| ICP/USDT:USDT | below_1h_threshold | +0.00% | +0.12% |
| LAB/USDT:USDT | below_1h_threshold | +0.00% | +0.12% |
| AERO/USDT:USDT | below_1h_threshold | +0.00% | +0.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
