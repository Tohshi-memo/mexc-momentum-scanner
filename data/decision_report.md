# Decision Report

- generated_at: 2026-09-03T02:51:44.071093+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13413**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.41% / filled 20/20。**
- 全期間 MARKET基準: n=13413, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.41% | **+0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.93% | **+1.18%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.54% | **+0.92%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.11% | **+0.82%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.75% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +6.25% | **+6.25%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.86% | **+0.43%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.52% | **+0.41%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$879.96** / 初期 $100.00 (+779.96%)
- 確定: 5000件 (Win 1516 / Loss 1638 / Flat 1846) / skip 4974件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $879.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$184.60** / 初期 $100.00 (+84.60%)
- 確定: 2372件 (Win 671 / Loss 576 / Flat 1125) / skip 4452件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0515 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $184.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.15** / 初期 $100.00 (+14.15%)
- 確定: 2115件 (Win 617 / Loss 832 / Flat 666) / pending 6件 / skip 2769件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000309 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $114.15

## 6. Latest Market Context

- 更新: 2026-09-03T02:51:25.041615+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.60% price=77781.4
- Funnel: target 1044 → liquid 157 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +33.52% | $75,624,201.80 |
| PONS/USDT:USDT | +23.25% | $4,353,254.52 |
| SNOWSTOCK/USDT:USDT | +22.82% | $1,461,709.22 |
| HEMI/USDT:USDT | +20.55% | $4,526,839.28 |
| MARSCOIN/USDT:USDT | +19.33% | $2,728,370.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUBARAK/USDT:USDT | below_1h_threshold | +4.78% | +4.18% |
| EGLD/USDT:USDT | below_1h_threshold | +3.81% | +3.22% |
| SUI/USDT:USDT | below_1h_threshold | +3.02% | +2.42% |
| USELESS/USDT:USDT | below_1h_threshold | +3.01% | +2.42% |
| OP/USDT:USDT | below_1h_threshold | +2.28% | +1.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
