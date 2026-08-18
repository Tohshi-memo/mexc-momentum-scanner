# Decision Report

- generated_at: 2026-08-18T18:36:20.674626+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11919**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.42% / filled 20/20。**
- 全期間 MARKET基準: n=11919, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.00% | **+0.90%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.69% | **+0.59%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.62% | **+0.52%** |
| MARKET | 20/20 | 100.0% | +0.42% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.40% | **+1.32%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.16% | **+0.97%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.10% | **+0.55%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.75% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.51** / 初期 $100.00 (+514.51%)
- 確定: 4210件 (Win 1295 / Loss 1375 / Flat 1540) / skip 4270件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.19% 残高後 $614.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1820件 (Win 502 / Loss 427 / Flat 891) / skip 3510件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0213 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.10** / 初期 $100.00 (+18.10%)
- 確定: 1723件 (Win 515 / Loss 657 / Flat 551) / pending 1件 / skip 1665件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000243 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.10

## 6. Latest Market Context

- 更新: 2026-08-18T18:36:12.160006+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=64756.3
- Funnel: target 993 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +5.09% | $16,583,465.79 |
| GPS/USDT:USDT | +3.86% | $21,490,093.91 |
| CYS/USDT:USDT | +2.80% | $13,947,552.14 |
| US/USDT:USDT | +2.73% | $1,049,148.37 |
| ATOM/USDT:USDT | +2.19% | $4,394,451.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.55% | +2.36% |
| ATOM/USDT:USDT | below_1h_threshold | +2.26% | +2.07% |
| FHE/USDT:USDT | below_1h_threshold | +2.11% | +1.92% |
| SKDD/USDT:USDT | below_1h_threshold | +1.49% | +1.30% |
| PRL/USDT:USDT | below_1h_threshold | +1.31% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
