# Decision Report

- generated_at: 2026-09-13T15:41:29.353648+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14449**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.37% / filled 20/20。**
- 全期間 MARKET基準: n=14449, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.37% | **+0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_BB3S | 2/13 | 15.4% | +3.39% | **+0.52%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.48% | **+0.43%** |
| LIMIT_ATR | 8/20 | 40.0% | +1.01% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.23% | **+0.18%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.69% | **-0.17%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | -0.31% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5432件 (Win 1635 / Loss 1760 / Flat 2037) / skip 5578件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$227.36** / 初期 $100.00 (+127.36%)
- 確定: 2967件 (Win 824 / Loss 706 / Flat 1437) / skip 4893件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0697 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: REZ/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $227.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.72** / 初期 $100.00 (+26.72%)
- 確定: 2856件 (Win 850 / Loss 1105 / Flat 901) / pending 0件 / skip 3064件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000292 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: REZ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.72

## 6. Latest Market Context

- 更新: 2026-09-13T15:41:15.989920+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=77042.5
- Funnel: target 1068 → liquid 135 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.8 >= 65=1, 4h RSI 72.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +265.86% | $103,754,151.81 |
| CVC/USDT:USDT | +64.27% | $4,770,921.47 |
| BTW/USDT:USDT | +26.82% | $6,602,065.47 |
| STEEM/USDT:USDT | +24.71% | $2,574,734.93 |
| ARK/USDT:USDT | +20.59% | $2,757,248.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FILECOIN/USDT:USDT | below_1h_threshold | +2.51% | +2.68% |
| ABNBSTOCK/USDT:USDT | below_1h_threshold | +1.10% | +1.27% |
| ICP/USDT:USDT | below_1h_threshold | +0.73% | +0.91% |
| STORJ/USDT:USDT | below_1h_threshold | +0.64% | +0.82% |
| ILV/USDT:USDT | below_1h_threshold | +0.29% | +0.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
