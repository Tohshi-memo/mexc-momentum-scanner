# Decision Report

- generated_at: 2026-07-17T10:16:14.494668+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8840**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.07% / filled 20/20。**
- 全期間 MARKET基準: n=8840, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_BB3S | 4/14 | 28.6% | +3.64% | **+1.04%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.87% | **+0.93%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.88% | **+0.66%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.44% | **+0.31%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.37% | **+0.30%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.60% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$111.81** / 初期 $100.00 (+11.81%)
- 確定トレード: 111件 (TP 42 / SL 65 / EXP 4)
- 最新: DODO/USDT:USDT TP_HIT PnL +8.00% 残高後 $111.81
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$344.05** / 初期 $100.00 (+244.05%)
- 確定: 2955件 (Win 921 / Loss 947 / Flat 1087) / skip 2446件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $344.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.25** / 初期 $100.00 (+8.25%)
- 確定: 802件 (Win 188 / Loss 171 / Flat 443) / skip 1449件
- 成長率目線: 平均log +0.000099 / 幾何平均 +0.010% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0322 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $108.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.37** / 初期 $100.00 (-1.63%)
- 確定: 107件 (Win 34 / Loss 69 / Flat 4) / pending 3件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000172 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $98.37

## 6. Latest Market Context

- 更新: 2026-07-17T10:16:06.763940+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=63071.1
- Funnel: target 885 → liquid 178 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BANK/USDT:USDT | +32.12% | $6,506,362.55 |
| XEC/USDT:USDT | +26.40% | $1,327,954.10 |
| LUMIA/USDT:USDT | +25.38% | $2,572,690.57 |
| LRC/USDT:USDT | +18.75% | $1,692,841.98 |
| KAITO/USDT:USDT | +15.76% | $4,465,628.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.42% | +3.25% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.36% | +2.19% |
| PI/USDT:USDT | below_1h_threshold | +1.48% | +1.30% |
| APDSTOCK/USDT:USDT | below_1h_threshold | +1.20% | +1.03% |
| LDO/USDT:USDT | below_1h_threshold | +1.05% | +0.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
