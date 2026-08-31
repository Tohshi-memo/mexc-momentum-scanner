# Decision Report

- generated_at: 2026-08-31T12:41:31.405163+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13173**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.58% / filled 20/20。**
- 全期間 MARKET基準: n=13173, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.58% | **+2.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.58% | **+2.58%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.16% | **+1.94%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.92% | **+0.65%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.16% | **+0.09%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.12% | **+0.06%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4876件 (Win 1485 / Loss 1609 / Flat 1782) / skip 4858件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.26** / 初期 $100.00 (+73.26%)
- 確定: 2170件 (Win 602 / Loss 528 / Flat 1040) / skip 4414件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0020 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 2084件 (Win 610 / Loss 812 / Flat 662) / pending 0件 / skip 2559件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000557 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-31T12:41:21.297599+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.63% price=77795.1
- Funnel: target 1028 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKR/USDT:USDT | +60.49% | $53,370,432.94 |
| HEMI/USDT:USDT | +44.42% | $8,155,077.93 |
| BASECAT/USDT:USDT | +33.90% | $2,035,955.17 |
| ZORA/USDT:USDT | +32.12% | $14,308,319.69 |
| 0G/USDT:USDT | +26.38% | $6,006,432.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEMI/USDT:USDT | below_1h_threshold | +2.72% | +3.34% |
| USELESS/USDT:USDT | below_1h_threshold | +1.66% | +2.28% |
| STX/USDT:USDT | below_1h_threshold | +0.85% | +1.48% |
| DESTOCK/USDT:USDT | below_1h_threshold | +0.78% | +1.41% |
| NGAS/USDT:USDT | below_1h_threshold | +0.76% | +1.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
