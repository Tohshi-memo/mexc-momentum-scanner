# Decision Report

- generated_at: 2026-08-22T22:46:24.553316+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12420**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.65% / filled 20/20。**
- 全期間 MARKET基準: n=12420, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.82% | **+0.85%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.65% | **+0.65%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +8.00% | **+3.20%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.00% | **+0.85%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +2.04% | **+0.51%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$706.22** / 初期 $100.00 (+606.22%)
- 確定: 4452件 (Win 1365 / Loss 1456 / Flat 1631) / skip 4529件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $706.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.53** / 初期 $100.00 (+56.53%)
- 確定: 1934件 (Win 533 / Loss 465 / Flat 936) / skip 3897件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PEPE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.84** / 初期 $100.00 (+16.84%)
- 確定: 1863件 (Win 549 / Loss 706 / Flat 608) / pending 0件 / skip 2032件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000285 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TUT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.84

## 6. Latest Market Context

- 更新: 2026-08-22T22:46:14.872954+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=77064.0
- Funnel: target 1018 → liquid 209 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.5 >= 65=1, 4h RSI 75.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +34.28% | $37,878,003.07 |
| CATE/USDT:USDT | +33.36% | $11,661,236.76 |
| ZRO/USDT:USDT | +15.15% | $7,974,674.68 |
| STX/USDT:USDT | +13.16% | $9,907,436.85 |
| SQD/USDT:USDT | +11.79% | $2,477,360.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.65% | +3.39% |
| FORM/USDT:USDT | below_1h_threshold | +3.63% | +3.37% |
| GALA/USDT:USDT | below_1h_threshold | +3.49% | +3.23% |
| PEOPLE/USDT:USDT | below_1h_threshold | +3.45% | +3.19% |
| SPK/USDT:USDT | below_1h_threshold | +2.78% | +2.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
