# Decision Report

- generated_at: 2026-09-11T12:51:29.905128+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14217**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.39% / filled 20/20。**
- 全期間 MARKET基準: n=14217, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.14% | **+0.43%** |
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.30% | **-0.18%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.68% | **-0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.66% | **+1.33%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.65% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,078.19** / 初期 $100.00 (+978.19%)
- 確定: 5382件 (Win 1621 / Loss 1740 / Flat 2021) / skip 5396件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.98% 残高後 $1,078.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.52** / 初期 $100.00 (+108.52%)
- 確定: 2804件 (Win 770 / Loss 650 / Flat 1384) / skip 4824件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $208.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.96** / 初期 $100.00 (+22.96%)
- 確定: 2720件 (Win 803 / Loss 1041 / Flat 876) / pending 6件 / skip 2964件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $122.96

## 6. Latest Market Context

- 更新: 2026-09-11T12:51:16.778170+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.27% price=77979.1
- Funnel: target 1068 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=3, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STONK/USDT:USDT | +74.98% | $1,107,466.98 |
| STORJ/USDT:USDT | +70.79% | $2,689,819.09 |
| NIULAI/USDT:USDT | +52.28% | $20,232,193.89 |
| MET/USDT:USDT | +24.88% | $1,330,714.25 |
| RAY/USDT:USDT | +23.47% | $22,237,659.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAY/USDT:USDT | below_relative_strength | +6.05% | +4.78% |
| PONS/USDT:USDT | below_relative_strength | +5.14% | +3.87% |
| PENDLE/USDT:USDT | below_relative_strength | +5.12% | +3.85% |
| SPX/USDT:USDT | below_1h_threshold | +4.82% | +3.55% |
| NEAR/USDT:USDT | below_1h_threshold | +4.27% | +3.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
