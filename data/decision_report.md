# Decision Report

- generated_at: 2026-09-12T22:26:22.673812+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14326**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.76% / filled 20/20。**
- 全期間 MARKET基準: n=14326, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.76% | **+1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.76% | **+1.76%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.29% | **+1.16%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.43% | **+0.50%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.06% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.96% | **+0.87%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.59% | **+0.47%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.01% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5429件 (Win 1635 / Loss 1760 / Flat 2034) / skip 5458件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$211.97** / 初期 $100.00 (+111.97%)
- 確定: 2844件 (Win 784 / Loss 660 / Flat 1400) / skip 4893件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1407 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $211.97

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.95** / 初期 $100.00 (+23.95%)
- 確定: 2777件 (Win 822 / Loss 1068 / Flat 887) / pending 2件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000431 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $123.95

## 6. Latest Market Context

- 更新: 2026-09-12T22:26:11.061220+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=77229.7
- Funnel: target 1068 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +19.06% | $9,736,225.01 |
| STORJ/USDT:USDT | +18.98% | $22,611,347.83 |
| REZ/USDT:USDT | +15.58% | $1,902,692.13 |
| RIVER/USDT:USDT | +10.71% | $15,169,704.81 |
| ALCH/USDT:USDT | +10.08% | $1,971,947.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALCH/USDT:USDT | below_1h_threshold | +0.82% | +0.81% |
| FLOCK/USDT:USDT | below_1h_threshold | +0.81% | +0.80% |
| REZ/USDT:USDT | below_1h_threshold | +0.69% | +0.68% |
| IOST/USDT:USDT | below_1h_threshold | +0.68% | +0.67% |
| AKE/USDT:USDT | below_1h_threshold | +0.57% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
