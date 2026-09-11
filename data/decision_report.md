# Decision Report

- generated_at: 2026-09-11T17:51:22.932286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14241**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.24% / filled 20/20。**
- 全期間 MARKET基準: n=14241, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/16 | 12.5% | +3.28% | **+0.41%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.02% | **+0.31%** |
| MARKET | 20/20 | 100.0% | +0.24% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +5.30% | **+3.97%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.75% | **+1.23%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.89% | **+0.71%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.85% | **+0.64%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 210件 (TP 78 / SL 127 / EXP 5)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,095.58** / 初期 $100.00 (+995.58%)
- 確定: 5399件 (Win 1628 / Loss 1747 / Flat 2024) / skip 5403件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.45% 残高後 $1,095.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2817件 (Win 775 / Loss 655 / Flat 1387) / skip 4835件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0534 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.30% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.70** / 初期 $100.00 (+23.70%)
- 確定: 2733件 (Win 809 / Loss 1047 / Flat 877) / pending 5件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000334 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MINA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $123.70

## 6. Latest Market Context

- 更新: 2026-09-11T17:51:11.972615+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.47% price=77515.9
- Funnel: target 1067 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +11.59% | $4,658,231.43 |
| STORJ/USDT:USDT | +9.82% | $6,411,967.81 |
| BEAT/USDT:USDT | +4.45% | $7,683,354.30 |
| HNT/USDT:USDT | +4.31% | $1,904,349.56 |
| STONK/USDT:USDT | +2.53% | $1,387,570.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +4.58% | +5.05% |
| LAB/USDT:USDT | below_1h_threshold | +3.74% | +4.21% |
| HNT/USDT:USDT | below_1h_threshold | +2.91% | +3.38% |
| WLFI/USDT:USDT | below_1h_threshold | +2.49% | +2.96% |
| BEAT/USDT:USDT | below_1h_threshold | +2.30% | +2.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
