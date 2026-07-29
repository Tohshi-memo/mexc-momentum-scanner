# Decision Report

- generated_at: 2026-07-29T03:36:30.172736+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9762**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.58% / filled 20/20。**
- 全期間 MARKET基準: n=9762, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+3.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.58% | **+3.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.58% | **+3.58%** |
| LIMIT_ATR | 14/20 | 70.0% | +3.92% | **+2.75%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.28% | **+2.63%** |
| LIMIT_2PCT | 12/20 | 60.0% | +3.15% | **+1.89%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.93% | **+1.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 15/20 | 75.0% | +0.98% | **+0.74%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +2.01% | **+0.20%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.22% | **+0.12%** |
| LIMIT_FIB1618_LONG | 10/20 | 50.0% | -0.59% | **-0.30%** |

## 2. $100 Live Portfolio

- 残高: **$118.69** / 初期 $100.00 (+18.69%)
- 確定トレード: 160件 (TP 62 / SL 93 / EXP 5)
- 最新: ZHIPUSTOCK/USDT:USDT TP_HIT PnL +6.35% 残高後 $118.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2804件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1227件 (Win 338 / Loss 275 / Flat 614) / skip 1946件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0204 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.16** / 初期 $100.00 (+10.16%)
- 確定: 760件 (Win 246 / Loss 291 / Flat 223) / pending 0件 / skip 474件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000393 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $110.16

## 6. Latest Market Context

- 更新: 2026-07-29T03:36:16.797225+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=63741.4
- Funnel: target 904 → liquid 169 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +44.20% | $1,329,302.53 |
| BTW/USDT:USDT | +30.22% | $6,861,245.41 |
| KAITO/USDT:USDT | +12.71% | $9,759,538.16 |
| BEAT/USDT:USDT | +12.40% | $44,877,696.11 |
| EUL/USDT:USDT | +10.38% | $2,656,214.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +3.58% | +3.91% |
| UB/USDT:USDT | below_1h_threshold | +1.53% | +1.86% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +0.79% | +1.12% |
| RCATSTOCK/USDT:USDT | below_1h_threshold | +0.65% | +0.98% |
| AAPLSTOCK/USDT:USDT | below_1h_threshold | +0.23% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
