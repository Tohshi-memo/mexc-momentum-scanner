# Decision Report

- generated_at: 2026-08-14T18:01:30.596348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11587**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11587, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.97% | **+0.89%** |
| LIMIT_3PCT | 19/20 | 95.0% | +0.91% | **+0.87%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.51% | **+0.36%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.66% | **+2.53%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.65% | **+1.64%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.05% | **+1.44%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.94% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$644.75** / 初期 $100.00 (+544.75%)
- 確定: 4055件 (Win 1273 / Loss 1332 / Flat 1450) / skip 4093件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $644.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.77** / 初期 $100.00 (+52.77%)
- 確定: 1655件 (Win 475 / Loss 398 / Flat 782) / skip 3343件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0677 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $152.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.23** / 初期 $100.00 (+17.23%)
- 確定: 1541件 (Win 468 / Loss 589 / Flat 484) / pending 6件 / skip 1515件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000260 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.23

## 6. Latest Market Context

- 更新: 2026-08-14T18:01:20.591028+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=62985.0
- Funnel: target 985 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +15.34% | $69,245,087.86 |
| ACE/USDT:USDT | +10.48% | $54,279,106.77 |
| CAP/USDT:USDT | +8.86% | $13,943,737.25 |
| US/USDT:USDT | +8.70% | $5,929,862.10 |
| AVNT/USDT:USDT | +5.74% | $2,711,321.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.65% |
| TESLA/USDT:USDT | below_1h_threshold | +0.93% | +0.93% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.71% | +0.72% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.58% | +0.59% |
| BANK/USDT:USDT | below_1h_threshold | +0.49% | +0.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
