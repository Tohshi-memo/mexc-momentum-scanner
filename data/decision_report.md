# Decision Report

- generated_at: 2026-08-07T13:46:40.386570+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10717**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.61% / filled 20/20。**
- 全期間 MARKET基準: n=10717, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.61% | **+1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.90% | **+1.71%** |
| MARKET | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.26% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.07% | **-0.03%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | -0.10% | **-0.05%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | -0.13% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3798件 (Win 1203 / Loss 1250 / Flat 1345) / skip 3480件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1456件 (Win 407 / Loss 342 / Flat 707) / skip 2672件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.47** / 初期 $100.00 (+18.47%)
- 確定: 1168件 (Win 377 / Loss 458 / Flat 333) / pending 5件 / skip 1023件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000408 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DKNGSTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.47

## 6. Latest Market Context

- 更新: 2026-08-07T13:46:22.133130+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=65248.0
- Funnel: target 961 → liquid 196 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +36.26% | $4,293,204.69 |
| BICO/USDT:USDT | +34.49% | $32,591,787.34 |
| KGEN/USDT:USDT | +32.90% | $2,766,666.32 |
| C98/USDT:USDT | +32.58% | $1,610,779.61 |
| SKYAI/USDT:USDT | +31.56% | $79,746,803.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRVT/USDT:USDT | below_1h_threshold | +4.59% | +4.61% |
| CATE/USDT:USDT | below_1h_threshold | +3.76% | +3.78% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.79% | +2.81% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +2.58% |
| TWLOSTOCK/USDT:USDT | below_1h_threshold | +2.31% | +2.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
