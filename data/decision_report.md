# Decision Report

- generated_at: 2026-09-19T22:51:36.727138+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15104**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.06% / filled 20/20。**
- 全期間 MARKET基準: n=15104, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/18 | 33.3% | +3.82% | **+1.27%** |
| MARKET | 20/20 | 100.0% | +1.06% | **+1.06%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.01% | **+0.96%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.94% | **+0.80%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.83% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.10% | **+1.10%** |
| MARKET_LONG | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.07% | **+0.03%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | -0.00% | **-0.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | -0.29% | **-0.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,195.40** / 初期 $100.00 (+1095.40%)
- 確定: 5640件 (Win 1691 / Loss 1829 / Flat 2120) / skip 6025件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,195.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$244.24** / 初期 $100.00 (+144.24%)
- 確定: 3217件 (Win 891 / Loss 762 / Flat 1564) / skip 5298件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0255 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $244.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.01** / 初期 $100.00 (+22.01%)
- 確定: 2975件 (Win 880 / Loss 1176 / Flat 919) / pending 3件 / skip 3600件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000367 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.01

## 6. Latest Market Context

- 更新: 2026-09-19T22:51:22.608203+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=81184.2
- Funnel: target 1050 → liquid 141 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.6 >= 65=1, 4h RSI 67.8 >= 65=1, 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +48.93% | $42,475,578.03 |
| CELR/USDT:USDT | +47.71% | $1,091,621.85 |
| OFC/USDT:USDT | +47.02% | $1,728,543.75 |
| BANK/USDT:USDT | +15.90% | $2,457,589.21 |
| PIEVERSE/USDT:USDT | +13.97% | $1,097,134.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_relative_strength | +5.04% | +4.90% |
| STRK/USDT:USDT | below_1h_threshold | +4.50% | +4.36% |
| INJ/USDT:USDT | below_1h_threshold | +2.47% | +2.32% |
| WLD/USDT:USDT | below_1h_threshold | +1.83% | +1.68% |
| OFC/USDT:USDT | below_1h_threshold | +1.80% | +1.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
