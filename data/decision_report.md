# Decision Report

- generated_at: 2026-10-05T14:11:26.824319+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16161**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=16161, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/11 | 36.4% | +2.62% | **+0.95%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.02% | **+0.77%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.13% | **+0.23%** |
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +0.05% | **+0.05%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -0.18% | **-0.04%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | -0.20% | **-0.13%** |

## 2. $100 Live Portfolio

- 残高: **$120.15** / 初期 $100.00 (+20.15%)
- 確定トレード: 230件 (TP 82 / SL 141 / EXP 7)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,305.64** / 初期 $100.00 (+1205.64%)
- 確定: 6220件 (Win 1824 / Loss 1988 / Flat 2408) / skip 6502件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKY/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,305.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3610件 (Win 1005 / Loss 845 / Flat 1760) / skip 5962件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0233 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4320件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-05T14:11:15.297279+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=86545.3
- Funnel: target 1074 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +103.26% | $12,352,815.25 |
| RLC/USDT:USDT | +50.78% | $3,156,098.98 |
| FLUID/USDT:USDT | +21.56% | $2,181,351.12 |
| MOVR/USDT:USDT | +14.65% | $10,649,023.99 |
| NIL/USDT:USDT | +12.06% | $10,425,840.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +3.63% | +3.45% |
| MOVR/USDT:USDT | below_1h_threshold | +1.68% | +1.49% |
| GRASS/USDT:USDT | below_1h_threshold | +1.59% | +1.41% |
| ORCA/USDT:USDT | below_1h_threshold | +1.48% | +1.29% |
| NIL/USDT:USDT | below_1h_threshold | +1.34% | +1.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
