# Decision Report

- generated_at: 2026-09-10T16:31:30.224599+00:00
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

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 207件 (TP 78 / SL 124 / EXP 5)
- 最新: HEMI/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.16
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
- 確定: 2675件 (Win 789 / Loss 1022 / Flat 864) / pending 6件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000375 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $122.17

## 6. Latest Market Context

- 更新: 2026-09-10T16:31:19.093813+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=76939.8
- Funnel: target 1067 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.0 >= 65=1, 4h RSI 66.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +8.57% | $1,274,510.81 |
| NES/USDT:USDT | +8.05% | $1,771,085.74 |
| BTW/USDT:USDT | +2.99% | $1,500,014.24 |
| BTR/USDT:USDT | +1.91% | $4,403,314.62 |
| BULLA/USDT:USDT | +1.76% | $3,071,566.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.99% | +3.35% |
| BTR/USDT:USDT | below_1h_threshold | +1.90% | +2.26% |
| USOIL/USDT:USDT | below_1h_threshold | +1.88% | +2.24% |
| PONS/USDT:USDT | below_1h_threshold | +1.88% | +2.24% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.77% | +2.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
