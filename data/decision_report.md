# Decision Report

- generated_at: 2026-07-16T21:26:19.218251+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8823**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.86% / filled 20/20。**
- 全期間 MARKET基準: n=8823, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.82% | **+0.73%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.87% | **+0.72%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.41% | **+0.37%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.89% | **+1.01%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.33% | **+0.67%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +3.08% | **+0.31%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.26% | **+0.21%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.22% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$109.89** / 初期 $100.00 (+9.89%)
- 確定トレード: 107件 (TP 40 / SL 64 / EXP 3)
- 最新: ALLO/USDT:USDT EXPIRED PnL +6.44% 残高後 $109.89
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$343.73** / 初期 $100.00 (+243.73%)
- 確定: 2938件 (Win 916 / Loss 946 / Flat 1076) / skip 2446件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $343.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.06** / 初期 $100.00 (+7.06%)
- 確定: 785件 (Win 181 / Loss 171 / Flat 433) / skip 1449件
- 成長率目線: 平均log +0.000087 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0068 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $107.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$97.72** / 初期 $100.00 (-2.28%)
- 確定: 90件 (Win 26 / Loss 60 / Flat 4) / pending 2件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $97.72

## 6. Latest Market Context

- 更新: 2026-07-16T21:26:12.786720+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64132.4
- Funnel: target 880 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +18.32% | $2,039,615.46 |
| LRC/USDT:USDT | +11.81% | $1,026,041.10 |
| KAITO/USDT:USDT | +10.25% | $2,162,608.51 |
| DEXE/USDT:USDT | +8.64% | $3,636,332.00 |
| SLX/USDT:USDT | +6.52% | $1,776,024.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +1.82% | +1.75% |
| RIVER/USDT:USDT | below_1h_threshold | +1.56% | +1.49% |
| DOT/USDT:USDT | below_1h_threshold | +1.53% | +1.46% |
| POETSTOCK/USDT:USDT | below_1h_threshold | +1.52% | +1.46% |
| TRIA/USDT:USDT | below_1h_threshold | +1.39% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
