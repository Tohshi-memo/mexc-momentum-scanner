# Decision Report

- generated_at: 2026-08-05T00:36:26.531597+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10329**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.81% / filled 20/20。**
- 全期間 MARKET基準: n=10329, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.84% | **+1.29%** |
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.72% | **+0.77%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.88% | **+0.61%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +1.48% | **+0.96%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.23% | **+0.86%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.84% | **+0.68%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.20% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3727件 (Win 1179 / Loss 1222 / Flat 1326) / skip 3163件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2455件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0045 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.88** / 初期 $100.00 (+16.88%)
- 確定: 1086件 (Win 349 / Loss 423 / Flat 314) / pending 1件 / skip 714件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000224 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $116.88

## 6. Latest Market Context

- 更新: 2026-08-05T00:36:17.627745+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=64158.3
- Funnel: target 937 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +35.67% | $4,096,380.78 |
| CASHCAT/USDT:USDT | +32.50% | $1,113,270.67 |
| TAKE/USDT:USDT | +25.54% | $1,301,753.40 |
| HFT/USDT:USDT | +19.68% | $1,424,200.60 |
| BICO/USDT:USDT | +17.42% | $15,035,467.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.60% | +3.47% |
| SNXX/USDT:USDT | below_1h_threshold | +3.45% | +3.32% |
| CAP/USDT:USDT | below_1h_threshold | +2.99% | +2.87% |
| HFT/USDT:USDT | below_1h_threshold | +2.83% | +2.70% |
| NIL/USDT:USDT | below_1h_threshold | +2.44% | +2.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
