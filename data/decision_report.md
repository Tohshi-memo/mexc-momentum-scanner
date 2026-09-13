# Decision Report

- generated_at: 2026-09-13T09:56:33.616346+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14407**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=14407, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 2/15 | 13.3% | +3.31% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.68% | **+0.84%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.43% | **+0.37%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.46% | **+0.35%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.89% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5431件 (Win 1635 / Loss 1760 / Flat 2036) / skip 5537件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$223.18** / 初期 $100.00 (+123.18%)
- 確定: 2925件 (Win 813 / Loss 695 / Flat 1417) / skip 4893件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1003 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $223.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.62** / 初期 $100.00 (+26.62%)
- 確定: 2851件 (Win 848 / Loss 1102 / Flat 901) / pending 5件 / skip 3028件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.62

## 6. Latest Market Context

- 更新: 2026-09-13T09:56:20.395729+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=76750.0
- Funnel: target 1068 → liquid 133 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.8 >= 65=1, 4h RSI 74.2 >= 65=1, 4h RSI 95.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +212.93% | $90,696,244.74 |
| STEEM/USDT:USDT | +57.62% | $1,425,977.34 |
| ARK/USDT:USDT | +38.96% | $1,304,354.10 |
| VTHO/USDT:USDT | +37.33% | $3,304,551.41 |
| POWR/USDT:USDT | +29.29% | $2,545,163.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZCAT/USDT:USDT | below_1h_threshold | +4.90% | +4.92% |
| STORJ/USDT:USDT | below_1h_threshold | +4.38% | +4.41% |
| LONGXIA/USDT:USDT | below_1h_threshold | +4.38% | +4.40% |
| CRV/USDT:USDT | below_1h_threshold | +3.68% | +3.71% |
| THETA/USDT:USDT | below_1h_threshold | +3.06% | +3.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
