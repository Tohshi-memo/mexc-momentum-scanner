# Decision Report

- generated_at: 2026-09-13T14:46:18.934879+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14444**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.29% / filled 20/20。**
- 全期間 MARKET基準: n=14444, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.29% | **+0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 14/20 | 70.0% | +1.38% | **+0.96%** |
| LIMIT_BB3S | 2/12 | 16.7% | +3.39% | **+0.56%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.61% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.80% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5432件 (Win 1635 / Loss 1760 / Flat 2037) / skip 5573件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.96** / 初期 $100.00 (+128.96%)
- 確定: 2962件 (Win 824 / Loss 704 / Flat 1434) / skip 4893件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0921 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $228.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.94** / 初期 $100.00 (+26.94%)
- 確定: 2855件 (Win 850 / Loss 1104 / Flat 901) / pending 1件 / skip 3059件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000369 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UP/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.94

## 6. Latest Market Context

- 更新: 2026-09-13T14:46:08.111881+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=77209.9
- Funnel: target 1068 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +246.36% | $105,289,080.18 |
| CVC/USDT:USDT | +72.88% | $4,027,538.34 |
| STEEM/USDT:USDT | +32.72% | $2,454,862.50 |
| BTW/USDT:USDT | +27.30% | $5,993,786.27 |
| ARK/USDT:USDT | +24.38% | $2,640,583.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| REZ/USDT:USDT | below_1h_threshold | +3.92% | +3.41% |
| ZCAT/USDT:USDT | below_1h_threshold | +2.91% | +2.39% |
| BSV/USDT:USDT | below_1h_threshold | +2.46% | +1.94% |
| SAGA/USDT:USDT | below_1h_threshold | +1.96% | +1.45% |
| FLOCK/USDT:USDT | below_1h_threshold | +1.80% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
