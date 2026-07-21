# Decision Report

- generated_at: 2026-07-21T04:36:19.757440+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9152**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.90% / filled 20/20。**
- 全期間 MARKET基準: n=9152, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.90% | **+1.90%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.74% | **+0.59%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +2.52% | **+0.75%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.80% | **+0.72%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.57% | **+0.48%** |
| LIMIT_FIB1272_LONG | 14/20 | 70.0% | +0.56% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$108.05** / 初期 $100.00 (+8.05%)
- 確定トレード: 125件 (TP 44 / SL 76 / EXP 5)
- 最新: KIOXIASTOCK/USDT:USDT SL_HIT PnL -3.51% 残高後 $108.05
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$413.61** / 初期 $100.00 (+313.61%)
- 確定: 3214件 (Win 1007 / Loss 1024 / Flat 1183) / skip 2499件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $413.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$129.65** / 初期 $100.00 (+29.65%)
- 確定: 1113件 (Win 293 / Loss 232 / Flat 588) / skip 1450件
- 成長率目線: 平均log +0.000233 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0923 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $129.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.08** / 初期 $100.00 (+1.08%)
- 確定: 340件 (Win 120 / Loss 151 / Flat 69) / pending 1件 / skip 283件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000216 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: KIOXIASTOCK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.08

## 6. Latest Market Context

- 更新: 2026-07-21T04:36:11.981420+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=65499.8
- Funnel: target 885 → liquid 173 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ERA/USDT:USDT | +73.12% | $3,706,097.62 |
| JIMOTHY/USDT:USDT | +58.91% | $2,936,330.73 |
| ZHIPUSTOCK/USDT:USDT | +22.97% | $1,614,714.00 |
| LDO/USDT:USDT | +11.28% | $7,687,596.49 |
| BLESS/USDT:USDT | +10.34% | $2,319,326.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +3.95% | +4.01% |
| KORU/USDT:USDT | below_1h_threshold | +3.70% | +3.76% |
| SOXL/USDT:USDT | below_1h_threshold | +3.34% | +3.40% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.86% | +2.92% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.42% | +2.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
