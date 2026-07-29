# Decision Report

- generated_at: 2026-07-29T02:06:33.111657+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9753**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.89% / filled 20/20。**
- 全期間 MARKET基準: n=9753, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+4.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.89% | **+4.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.89% | **+4.89%** |
| LIMIT_1PCT | 15/20 | 75.0% | +4.19% | **+3.14%** |
| LIMIT_2PCT | 12/20 | 60.0% | +3.66% | **+2.20%** |
| LIMIT_ATR | 11/20 | 55.0% | +3.58% | **+1.97%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.97% | **+0.99%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 15/20 | 75.0% | -0.91% | **-0.69%** |
| LIMIT_FIB1618_LONG | 9/20 | 45.0% | -1.83% | **-0.82%** |
| LIMIT_6PCT_LONG | 15/20 | 75.0% | -2.09% | **-1.57%** |

## 2. $100 Live Portfolio

- 残高: **$116.35** / 初期 $100.00 (+16.35%)
- 確定トレード: 158件 (TP 60 / SL 93 / EXP 5)
- 最新: DRAM/USDT:USDT TP_HIT PnL +7.69% 残高後 $116.35
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$496.53** / 初期 $100.00 (+396.53%)
- 確定: 3518件 (Win 1113 / Loss 1146 / Flat 1259) / skip 2796件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOXL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $496.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1938件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0274 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.55** / 初期 $100.00 (+10.55%)
- 確定: 758件 (Win 246 / Loss 289 / Flat 223) / pending 2件 / skip 466件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KAITO/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $110.55

## 6. Latest Market Context

- 更新: 2026-07-29T02:06:26.493859+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63703.1
- Funnel: target 904 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +20.92% | $1,231,449.79 |
| ON/USDT:USDT | +16.00% | $51,916,779.43 |
| BEAT/USDT:USDT | +13.91% | $45,249,828.59 |
| BTW/USDT:USDT | +12.27% | $6,143,143.97 |
| KAITO/USDT:USDT | +9.77% | $9,466,621.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +2.21% | +2.17% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.98% | +1.95% |
| LA/USDT:USDT | below_1h_threshold | +1.41% | +1.38% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.75% | +0.72% |
| ALUMINUM/USDT:USDT | below_1h_threshold | +0.54% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
