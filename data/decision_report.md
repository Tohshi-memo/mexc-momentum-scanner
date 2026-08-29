# Decision Report

- generated_at: 2026-08-29T09:51:16.809908+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12920**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=12920, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.72% | **+0.69%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.51% | **+0.33%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.53% | **+0.47%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.45% | **+0.29%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.18% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.01% | **+0.01%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$717.71** / 初期 $100.00 (+617.71%)
- 確定: 4690件 (Win 1419 / Loss 1540 / Flat 1731) / skip 4791件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $717.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.75** / 初期 $100.00 (+56.75%)
- 確定: 2007件 (Win 546 / Loss 485 / Flat 976) / skip 4324件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0007 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $156.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.51** / 初期 $100.00 (+16.51%)
- 確定: 2015件 (Win 592 / Loss 777 / Flat 646) / pending 2件 / skip 2372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000363 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.51

## 6. Latest Market Context

- 更新: 2026-08-29T09:51:07.083306+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=77639.7
- Funnel: target 1023 → liquid 143 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.7 >= 65=1, 4h RSI 71.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +106.20% | $1,674,231.47 |
| HNT/USDT:USDT | +73.11% | $3,393,401.75 |
| ONG/USDT:USDT | +19.38% | $3,943,264.32 |
| O/USDT:USDT | +18.61% | $1,149,881.10 |
| COTI/USDT:USDT | +15.72% | $1,306,102.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TOAD/USDT:USDT | below_1h_threshold | +3.75% | +3.71% |
| RIVER/USDT:USDT | below_1h_threshold | +3.69% | +3.65% |
| TUT/USDT:USDT | below_1h_threshold | +3.07% | +3.03% |
| BMT/USDT:USDT | below_1h_threshold | +2.94% | +2.89% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.83% | +2.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
