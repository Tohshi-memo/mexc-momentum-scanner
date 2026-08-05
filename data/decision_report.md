# Decision Report

- generated_at: 2026-08-05T00:26:30.361847+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10328**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.41% / filled 20/20。**
- 全期間 MARKET基準: n=10328, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.01% | **+1.31%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.06% | **+0.96%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.72% | **+0.77%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.10% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.09% | **+0.76%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.77% | **+0.46%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.38% | **+0.26%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.43% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3163件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2454件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0043 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.48** / 初期 $100.00 (+16.48%)
- 確定: 1085件 (Win 348 / Loss 423 / Flat 314) / pending 1件 / skip 714件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000180 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.48

## 6. Latest Market Context

- 更新: 2026-08-05T00:26:21.271037+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=64002.2
- Funnel: target 937 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +31.75% | $4,050,876.78 |
| CASHCAT/USDT:USDT | +27.09% | $1,077,773.82 |
| TAKE/USDT:USDT | +25.40% | $1,294,095.05 |
| HFT/USDT:USDT | +16.68% | $1,417,371.59 |
| MARSCOIN/USDT:USDT | +14.77% | $1,016,213.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +3.45% | +3.56% |
| NIL/USDT:USDT | below_1h_threshold | +2.95% | +3.07% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.61% | +2.73% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.66% | +1.77% |
| CAP/USDT:USDT | below_1h_threshold | +1.62% | +1.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
