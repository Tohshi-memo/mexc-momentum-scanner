# Decision Report

- generated_at: 2026-10-13T01:46:28.084345+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16621**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=16621, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.53% | **+0.69%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_9PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_8PCT | 6/20 | 30.0% | +0.57% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.51% | **+0.46%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |
| LIMIT_BB3S_LONG | 5/12 | 41.7% | +0.80% | **+0.33%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.75** / 初期 $100.00 (+1191.75%)
- 確定: 6293件 (Win 1845 / Loss 2016 / Flat 2432) / skip 6889件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STX/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,291.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$272.12** / 初期 $100.00 (+172.12%)
- 確定: 3639件 (Win 1010 / Loss 855 / Flat 1774) / skip 6393件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RSR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $272.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4782件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-13T01:46:13.752564+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.18% price=82354.6
- Funnel: target 1089 → liquid 188 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=4, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CT/USDT:USDT | +9.98% | $2,791,914.49 |
| SOXS/USDT:USDT | +6.90% | $43,258,561.15 |
| STX/USDT:USDT | +5.52% | $14,103,153.57 |
| BTW/USDT:USDT | +4.05% | $13,654,527.55 |
| RENDER/USDT:USDT | +3.65% | $16,339,952.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_relative_strength | +5.72% | +4.54% |
| SAFE/USDT:USDT | below_relative_strength | +5.33% | +4.15% |
| CT/USDT:USDT | below_relative_strength | +5.26% | +4.08% |
| KAIA/USDT:USDT | below_relative_strength | +5.17% | +3.99% |
| RED/USDT:USDT | below_1h_threshold | +4.38% | +3.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
