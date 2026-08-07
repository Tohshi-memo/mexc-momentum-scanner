# Decision Report

- generated_at: 2026-08-07T13:31:46.786324+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10712**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.53% / filled 20/20。**
- 全期間 MARKET基準: n=10712, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.53% | **+0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.04% | **+0.98%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.39% | **+0.69%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.55% | **+0.38%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.40% | **+0.36%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.46% | **+0.27%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.18% | **+0.11%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3798件 (Win 1203 / Loss 1250 / Flat 1345) / skip 3475件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1456件 (Win 407 / Loss 342 / Flat 707) / skip 2667件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.87** / 初期 $100.00 (+17.87%)
- 確定: 1165件 (Win 375 / Loss 457 / Flat 333) / pending 6件 / skip 1021件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000456 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.87

## 6. Latest Market Context

- 更新: 2026-08-07T13:31:31.219215+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=65112.4
- Funnel: target 961 → liquid 195 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.5 >= 65=1, 4h RSI 65.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| C98/USDT:USDT | +36.02% | $1,540,293.35 |
| CATE/USDT:USDT | +34.77% | $4,193,034.17 |
| BICO/USDT:USDT | +33.87% | $32,102,081.82 |
| SKYAI/USDT:USDT | +32.82% | $78,745,754.75 |
| TUT/USDT:USDT | +28.35% | $1,169,760.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +4.89% | +5.12% |
| CATE/USDT:USDT | below_1h_threshold | +2.94% | +3.16% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.79% | +3.02% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +2.79% |
| TWLOSTOCK/USDT:USDT | below_1h_threshold | +2.31% | +2.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
