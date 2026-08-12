# Decision Report

- generated_at: 2026-08-12T09:31:25.597482+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11355**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11355, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.19% | **+2.87%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.06% | **+1.84%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.35% | **+1.51%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$624.58** / 初期 $100.00 (+524.58%)
- 確定: 3942件 (Win 1232 / Loss 1285 / Flat 1425) / skip 3974件
- 成長率目線: 平均log +0.000465 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $624.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.91** / 初期 $100.00 (+49.91%)
- 確定: 1591件 (Win 449 / Loss 369 / Flat 773) / skip 3175件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1058 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $149.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.71** / 初期 $100.00 (+14.71%)
- 確定: 1370件 (Win 413 / Loss 532 / Flat 425) / pending 2件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000222 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $114.71

## 6. Latest Market Context

- 更新: 2026-08-12T09:31:15.859326+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=64007.1
- Funnel: target 967 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +78.88% | $2,853,748.58 |
| JIMOTHY/USDT:USDT | +62.54% | $2,619,355.01 |
| PROM/USDT:USDT | +51.07% | $7,996,043.41 |
| BR/USDT:USDT | +44.51% | $1,846,918.95 |
| BEAT/USDT:USDT | +29.53% | $91,802,419.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROM/USDT:USDT | below_1h_threshold | +2.92% | +2.54% |
| JTO/USDT:USDT | below_1h_threshold | +2.90% | +2.53% |
| ALLO/USDT:USDT | below_1h_threshold | +2.88% | +2.50% |
| MUU/USDT:USDT | below_1h_threshold | +2.75% | +2.38% |
| SNXX/USDT:USDT | below_1h_threshold | +2.66% | +2.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
