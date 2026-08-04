# Decision Report

- generated_at: 2026-08-04T23:56:25.224953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10325**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=10325, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.73% | **+1.21%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.96% | **+0.67%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.92% | **+0.51%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.09% | **+3.09%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +2.01% | **+1.31%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.33% | **+0.86%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.56% | **+0.86%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.83% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3726件 (Win 1179 / Loss 1222 / Flat 1325) / skip 3160件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2451件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0553 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.09** / 初期 $100.00 (+17.09%)
- 確定: 1082件 (Win 348 / Loss 420 / Flat 314) / pending 3件 / skip 714件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000291 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.09

## 6. Latest Market Context

- 更新: 2026-08-04T23:56:18.381273+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=64093.2
- Funnel: target 937 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1, 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +33.40% | $3,899,114.75 |
| MARSCOIN/USDT:USDT | +26.03% | $1,005,647.54 |
| TAKE/USDT:USDT | +24.56% | $1,262,197.44 |
| CASHCAT/USDT:USDT | +20.04% | $1,069,581.26 |
| BICO/USDT:USDT | +16.16% | $15,116,160.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALABSTOCK/USDT:USDT | below_1h_threshold | +1.05% | +1.28% |
| BEAT/USDT:USDT | below_1h_threshold | +0.98% | +1.20% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.93% | +1.15% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.80% | +1.02% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.63% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
