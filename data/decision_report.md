# Decision Report

- generated_at: 2026-10-10T14:06:13.471659+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16495**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.13% / filled 20/20。**
- 全期間 MARKET基準: n=16495, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.13% | **+3.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.13% | **+3.13%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.64% | **+1.85%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.79% | **+1.34%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.18% | **+0.10%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.25% | **+0.16%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.26% | **+0.16%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.27% | **-0.07%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.61% | **-0.09%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | -0.60% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,298.24** / 初期 $100.00 (+1198.24%)
- 確定: 6287件 (Win 1845 / Loss 2015 / Flat 2427) / skip 6769件
- 成長率目線: 平均log +0.000408 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CFX/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.39% 残高後 $1,298.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3636件 (Win 1010 / Loss 853 / Flat 1773) / skip 6270件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MINA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4653件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000415 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-10T14:06:04.205510+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=82740.1
- Funnel: target 1087 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LUMIA/USDT:USDT | +44.37% | $4,085,846.85 |
| ERA/USDT:USDT | +31.71% | $1,286,937.46 |
| CAP/USDT:USDT | +25.42% | $3,526,336.58 |
| MAGIC/USDT:USDT | +15.81% | $26,178,270.15 |
| NEAR/USDT:USDT | +12.90% | $175,145,145.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ERA/USDT:USDT | below_1h_threshold | +0.87% | +0.93% |
| ZRX/USDT:USDT | below_1h_threshold | +0.39% | +0.45% |
| IMX/USDT:USDT | below_1h_threshold | +0.35% | +0.41% |
| PHA/USDT:USDT | below_1h_threshold | +0.25% | +0.31% |
| MAGIC/USDT:USDT | below_1h_threshold | +0.24% | +0.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
