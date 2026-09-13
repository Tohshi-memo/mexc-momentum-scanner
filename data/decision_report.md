# Decision Report

- generated_at: 2026-09-13T13:56:38.541318+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14439**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=14439, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +2.20% | **+1.76%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.53% | **+0.51%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.49% | **+0.42%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.41% | **+1.13%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.80% | **+0.67%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.82% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5432件 (Win 1635 / Loss 1760 / Flat 2037) / skip 5568件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.62** / 初期 $100.00 (+128.62%)
- 確定: 2957件 (Win 823 / Loss 704 / Flat 1430) / skip 4893件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0732 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CVC/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $228.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.94** / 初期 $100.00 (+26.94%)
- 確定: 2855件 (Win 850 / Loss 1104 / Flat 901) / pending 1件 / skip 3057件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000358 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UP/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.94

## 6. Latest Market Context

- 更新: 2026-09-13T13:56:22.644908+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=76826.4
- Funnel: target 1068 → liquid 133 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.8 >= 65=1, 4h RSI 85.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +264.59% | $105,806,055.06 |
| CVC/USDT:USDT | +81.71% | $2,486,671.72 |
| STEEM/USDT:USDT | +42.70% | $2,367,666.80 |
| ARK/USDT:USDT | +33.19% | $2,488,513.97 |
| VTHO/USDT:USDT | +24.20% | $3,436,817.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_1h_threshold | +4.66% | +4.53% |
| KOMA/USDT:USDT | below_1h_threshold | +2.87% | +2.74% |
| STEEM/USDT:USDT | below_1h_threshold | +2.81% | +2.68% |
| INJ/USDT:USDT | below_1h_threshold | +2.57% | +2.44% |
| REZ/USDT:USDT | below_1h_threshold | +1.95% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
