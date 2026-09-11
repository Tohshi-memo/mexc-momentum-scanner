# Decision Report

- generated_at: 2026-09-11T19:36:18.060127+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14250**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14250, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.11% | **+0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.01% | **+0.35%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +2.08% | **+0.21%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| MARKET | 20/20 | 100.0% | +0.11% | **+0.11%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +5.88% | **+3.92%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.55% | **+1.47%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.58% | **+1.34%** |
| MARKET_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.77% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,119.36** / 初期 $100.00 (+1019.36%)
- 確定: 5407件 (Win 1632 / Loss 1749 / Flat 2026) / skip 5404件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,119.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$210.13** / 初期 $100.00 (+110.13%)
- 確定: 2822件 (Win 777 / Loss 655 / Flat 1390) / skip 4839件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0065 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $210.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.45** / 初期 $100.00 (+24.45%)
- 確定: 2742件 (Win 813 / Loss 1050 / Flat 879) / pending 5件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000311 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $124.45

## 6. Latest Market Context

- 更新: 2026-09-11T19:36:09.982352+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=77209.0
- Funnel: target 1067 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +47.12% | $9,629,043.08 |
| LAB/USDT:USDT | +17.90% | $7,594,450.59 |
| BEAT/USDT:USDT | +12.25% | $9,455,760.95 |
| RIVER/USDT:USDT | +8.22% | $3,624,118.23 |
| MET/USDT:USDT | +3.92% | $1,860,813.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +3.14% | +2.89% |
| RIVER/USDT:USDT | below_1h_threshold | +2.94% | +2.69% |
| EGLD/USDT:USDT | below_1h_threshold | +2.33% | +2.09% |
| HPQSTOCK/USDT:USDT | below_1h_threshold | +2.08% | +1.83% |
| MINA/USDT:USDT | below_1h_threshold | +2.07% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
