# Decision Report

- generated_at: 2026-11-14T05:21:17.109787+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18877**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.26% / filled 20/20。**
- 全期間 MARKET基準: n=18877, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.26% | **+2.26%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.85% | **+1.67%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.71% | **+1.02%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.10% | **-0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,763.10** / 初期 $100.00 (+1663.10%)
- 確定: 7291件 (Win 2100 / Loss 2337 / Flat 2854) / skip 8147件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,763.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$416.29** / 初期 $100.00 (+316.29%)
- 確定: 4885件 (Win 1309 / Loss 1078 / Flat 2498) / skip 7403件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1394 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $416.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7034件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000373 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-14T05:21:05.795986+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=67174.5
- Funnel: target 1084 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHELL/USDT:USDT | +41.09% | $3,848,346.40 |
| BERA/USDT:USDT | +21.24% | $1,885,841.57 |
| AKE/USDT:USDT | +20.52% | $79,056,237.03 |
| UAI/USDT:USDT | +8.52% | $3,047,491.23 |
| NIGHT/USDT:USDT | +4.09% | $1,206,046.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +2.50% | +2.33% |
| SHELL/USDT:USDT | below_1h_threshold | +1.20% | +1.02% |
| RENDER/USDT:USDT | below_1h_threshold | +0.59% | +0.42% |
| JUP/USDT:USDT | below_1h_threshold | +0.19% | +0.02% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.17% | -0.01% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
