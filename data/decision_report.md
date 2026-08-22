# Decision Report

- generated_at: 2026-08-22T06:26:19.643330+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12351**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.68% / filled 20/20。**
- 全期間 MARKET基準: n=12351, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+3.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.68% | **+3.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.68% | **+3.68%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.82% | **+2.26%** |
| LIMIT_ATR | 12/20 | 60.0% | +3.13% | **+1.88%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.64% | **+0.99%** |
| LIMIT_BB3S | 8/15 | 53.3% | +1.56% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_10PCT_LONG | 10/20 | 50.0% | +0.09% | **+0.05%** |
| LIMIT_9PCT_LONG | 11/20 | 55.0% | -0.38% | **-0.21%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | -0.44% | **-0.31%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | -0.79% | **-0.55%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$716.07** / 初期 $100.00 (+616.07%)
- 確定: 4447件 (Win 1364 / Loss 1453 / Flat 1630) / skip 4465件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $716.07

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1934件 (Win 533 / Loss 465 / Flat 936) / skip 3828件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0036 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.04** / 初期 $100.00 (+17.04%)
- 確定: 1862件 (Win 549 / Loss 705 / Flat 608) / pending 0件 / skip 1959件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000556 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.04

## 6. Latest Market Context

- 更新: 2026-08-22T06:26:08.794531+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=77365.8
- Funnel: target 1018 → liquid 251 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +219.89% | $5,211,009.84 |
| TRUMPOFFICIAL/USDT:USDT | +57.07% | $99,265,357.68 |
| CATE/USDT:USDT | +46.74% | $11,590,180.41 |
| AGI/USDT:USDT | +36.36% | $2,004,459.18 |
| MELANIA/USDT:USDT | +34.17% | $1,488,873.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +2.24% | +2.24% |
| XRP/USDT:USDT | below_1h_threshold | +2.21% | +2.21% |
| CVX/USDT:USDT | below_1h_threshold | +2.08% | +2.09% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.87% | +1.88% |
| STX/USDT:USDT | below_1h_threshold | +1.55% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
