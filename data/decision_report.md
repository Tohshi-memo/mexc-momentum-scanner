# Decision Report

- generated_at: 2026-07-21T08:21:21.799425+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9164**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9164, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_BB3S | 7/15 | 46.7% | +0.15% | **+0.07%** |
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.04% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.46% | **+1.17%** |
| MARKET_LONG | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.44% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$427.35** / 初期 $100.00 (+327.35%)
- 確定: 3226件 (Win 1014 / Loss 1027 / Flat 1185) / skip 2499件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $427.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$132.54** / 初期 $100.00 (+32.54%)
- 確定: 1125件 (Win 300 / Loss 235 / Flat 590) / skip 1450件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0872 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $132.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 341件 (Win 120 / Loss 152 / Flat 69) / pending 0件 / skip 297件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000289 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T08:21:13.753729+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=66280.0
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +108.43% | $4,149,486.79 |
| ERA/USDT:USDT | +57.92% | $6,409,664.07 |
| ZHIPUSTOCK/USDT:USDT | +35.06% | $2,918,900.41 |
| DEXE/USDT:USDT | +19.64% | $2,575,638.91 |
| ESPORTS/USDT:USDT | +11.32% | $5,310,603.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.90% | +4.73% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.75% | +2.58% |
| ERA/USDT:USDT | below_1h_threshold | +2.08% | +1.91% |
| BULLA/USDT:USDT | below_1h_threshold | +0.88% | +0.71% |
| SNXX/USDT:USDT | below_1h_threshold | +0.57% | +0.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
