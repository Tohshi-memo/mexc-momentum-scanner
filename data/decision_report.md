# Decision Report

- generated_at: 2026-09-30T06:51:27.663957+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15817**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=15817, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.26% | **+1.36%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.58% | **+1.34%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.45% | **+0.11%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.04% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5987件 (Win 1766 / Loss 1925 / Flat 2296) / skip 6391件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRASS/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3535件 (Win 974 / Loss 812 / Flat 1749) / skip 5693件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0372 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3978件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-30T06:51:16.513153+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=82942.8
- Funnel: target 1073 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +82.73% | $7,076,438.54 |
| QNT/USDT:USDT | +16.29% | $363,060,093.41 |
| PHA/USDT:USDT | +16.00% | $3,973,737.05 |
| STONK/USDT:USDT | +14.41% | $1,302,200.09 |
| SOONNETWORK/USDT:USDT | +12.19% | $4,885,182.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PHA/USDT:USDT | below_1h_threshold | +2.74% | +3.23% |
| SI/USDT:USDT | below_1h_threshold | +2.36% | +2.84% |
| QNT/USDT:USDT | below_1h_threshold | +2.15% | +2.64% |
| AXS/USDT:USDT | below_1h_threshold | +0.87% | +1.35% |
| SOXS/USDT:USDT | below_1h_threshold | +0.72% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
