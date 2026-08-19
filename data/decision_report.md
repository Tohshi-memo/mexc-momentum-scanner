# Decision Report

- generated_at: 2026-08-19T15:46:34.464905+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11988**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +5.00% / filled 20/20。**
- 全期間 MARKET基準: n=11988, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+5.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +5.00% | **+5.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +5.00% | **+5.00%** |
| LIMIT_1PCT | 11/20 | 55.0% | +3.14% | **+1.73%** |
| LIMIT_BB3S | 6/20 | 30.0% | +2.70% | **+0.81%** |
| LIMIT_2PCT | 8/20 | 40.0% | +1.95% | **+0.78%** |
| LIMIT_3PCT | 6/20 | 30.0% | +1.71% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.29% | **+0.19%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | +0.04% | **+0.03%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -2.19% | **-0.55%** |
| LIMIT_7PCT_LONG | 14/20 | 70.0% | -1.17% | **-0.82%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$605.47** / 初期 $100.00 (+505.47%)
- 確定: 4241件 (Win 1302 / Loss 1388 / Flat 1551) / skip 4308件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MUU/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $605.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3578件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.97** / 初期 $100.00 (+16.97%)
- 確定: 1753件 (Win 520 / Loss 669 / Flat 564) / pending 0件 / skip 1706件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000392 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.97

## 6. Latest Market Context

- 更新: 2026-08-19T15:46:24.270334+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +3.92% price=68481.9
- Funnel: target 999 → liquid 190 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=43, below_relative_strength=5, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +59.67% | $123,872,602.07 |
| MUBARAK/USDT:USDT | +40.52% | $1,643,286.81 |
| HEMI/USDT:USDT | +36.54% | $6,566,277.88 |
| UNITREE/USDT:USDT | +19.17% | $18,184,997.64 |
| STAR/USDT:USDT | +18.42% | $1,132,919.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_relative_strength | +6.16% | +2.23% |
| BR/USDT:USDT | below_relative_strength | +5.92% | +2.00% |
| MSTRSTOCK/USDT:USDT | below_relative_strength | +5.90% | +1.98% |
| COINBASE/USDT:USDT | below_relative_strength | +5.80% | +1.88% |
| ETH/USDT:USDT | below_relative_strength | +5.64% | +1.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
