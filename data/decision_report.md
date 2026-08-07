# Decision Report

- generated_at: 2026-08-07T09:41:23.796150+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10697**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.41% / filled 20/20。**
- 全期間 MARKET基準: n=10697, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 9/20 | 45.0% | +3.11% | **+1.40%** |
| LIMIT_3PCT | 17/20 | 85.0% | +1.25% | **+1.06%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.85% | **+0.77%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +2.72% | **+1.36%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.10% | **+1.36%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.15% | **+0.86%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3798件 (Win 1203 / Loss 1250 / Flat 1345) / skip 3460件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.49** / 初期 $100.00 (+44.49%)
- 確定: 1455件 (Win 407 / Loss 342 / Flat 706) / skip 2653件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.08% 残高後 $144.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.67** / 初期 $100.00 (+16.67%)
- 確定: 1159件 (Win 371 / Loss 455 / Flat 333) / pending 0件 / skip 1013件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000278 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKAMSTOCK/USDT:USDT `MARKET` EXPIRED account +0.09% 残高後 $116.67

## 6. Latest Market Context

- 更新: 2026-08-07T09:41:15.570141+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.48% price=64888.1
- Funnel: target 961 → liquid 190 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +30.98% | $4,372,268.09 |
| SKYAI/USDT:USDT | +27.24% | $67,794,244.01 |
| BICO/USDT:USDT | +27.23% | $23,961,488.33 |
| HEI/USDT:USDT | +22.02% | $50,637,026.51 |
| ON/USDT:USDT | +20.85% | $11,257,933.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AAOISTOCK/USDT:USDT | below_relative_strength | +5.44% | +4.95% |
| SNXX/USDT:USDT | below_1h_threshold | +2.94% | +2.46% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.71% | +2.23% |
| ALLO/USDT:USDT | below_1h_threshold | +2.67% | +2.19% |
| HEI/USDT:USDT | below_1h_threshold | +2.65% | +2.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
