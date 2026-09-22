# Decision Report

- generated_at: 2026-09-22T03:46:26.722446+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15291**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.43% / filled 20/20。**
- 全期間 MARKET基準: n=15291, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.43%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.96% | **+1.76%** |
| MARKET | 20/20 | 100.0% | +1.43% | **+1.43%** |
| LIMIT_BB3S | 7/16 | 43.8% | +2.35% | **+1.03%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.31% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.35% | **+0.31%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.18% | **+0.08%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.05% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,189.29** / 初期 $100.00 (+1089.29%)
- 確定: 5782件 (Win 1721 / Loss 1860 / Flat 2201) / skip 6070件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZETA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,189.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$250.46** / 初期 $100.00 (+150.46%)
- 確定: 3330件 (Win 921 / Loss 771 / Flat 1638) / skip 5372件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0424 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZETA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $250.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.20** / 初期 $100.00 (+23.20%)
- 確定: 3063件 (Win 902 / Loss 1198 / Flat 963) / pending 5件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000290 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZETA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $123.20

## 6. Latest Market Context

- 更新: 2026-09-22T03:46:13.678508+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=85444.8
- Funnel: target 1055 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KERNEL/USDT:USDT | +34.51% | $2,732,667.60 |
| ALCH/USDT:USDT | +18.13% | $2,431,049.28 |
| AKE/USDT:USDT | +13.74% | $35,333,173.77 |
| GRASS/USDT:USDT | +13.59% | $2,498,195.80 |
| FORM/USDT:USDT | +12.98% | $9,467,344.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.42% | +4.70% |
| PHA/USDT:USDT | below_1h_threshold | +4.18% | +4.46% |
| MUBARAK/USDT:USDT | below_1h_threshold | +3.14% | +3.42% |
| 4STOCK/USDT:USDT | below_1h_threshold | +3.02% | +3.30% |
| LAB/USDT:USDT | below_1h_threshold | +2.19% | +2.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
