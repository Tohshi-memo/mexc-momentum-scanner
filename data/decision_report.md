# Decision Report

- generated_at: 2026-09-10T16:16:26.029494+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14170**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.55% / filled 20/20。**
- 全期間 MARKET基準: n=14170, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.55% | **+0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +2.11% | **+1.05%** |
| LIMIT_BB3S | 4/19 | 21.1% | +3.88% | **+0.82%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.75% | **+0.71%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.50% | **+0.37%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.17% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,060.79** / 初期 $100.00 (+960.79%)
- 確定: 5350件 (Win 1609 / Loss 1728 / Flat 2013) / skip 5381件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,060.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$207.55** / 初期 $100.00 (+107.55%)
- 確定: 2764件 (Win 763 / Loss 649 / Flat 1352) / skip 4817件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1026 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $207.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.17** / 初期 $100.00 (+22.17%)
- 確定: 2675件 (Win 789 / Loss 1022 / Flat 864) / pending 5件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000375 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.17

## 6. Latest Market Context

- 更新: 2026-09-10T16:16:15.331128+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=76951.8
- Funnel: target 1067 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +8.41% | $1,737,232.73 |
| SAGA/USDT:USDT | +3.52% | $1,001,902.89 |
| BTW/USDT:USDT | +2.48% | $1,469,864.92 |
| SOPH/USDT:USDT | +2.28% | $2,337,382.09 |
| BTR/USDT:USDT | +2.04% | $4,389,253.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.53% | +3.87% |
| SOPH/USDT:USDT | below_1h_threshold | +2.58% | +2.93% |
| UAI/USDT:USDT | below_1h_threshold | +2.53% | +2.88% |
| BTW/USDT:USDT | below_1h_threshold | +2.49% | +2.83% |
| BTR/USDT:USDT | below_1h_threshold | +1.94% | +2.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
