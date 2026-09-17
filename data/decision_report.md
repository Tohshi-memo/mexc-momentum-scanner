# Decision Report

- generated_at: 2026-09-17T00:32:01.612999+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14754**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.21% / filled 20/20。**
- 全期間 MARKET基準: n=14754, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.61% | **+0.89%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.74% | **+0.66%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +2.18% | **+1.31%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.29% | **+0.58%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.32% | **+0.46%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.50% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,165.60** / 初期 $100.00 (+1065.60%)
- 確定: 5600件 (Win 1679 / Loss 1813 / Flat 2108) / skip 5715件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BRETT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,165.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$240.73** / 初期 $100.00 (+140.73%)
- 確定: 3129件 (Win 870 / Loss 746 / Flat 1513) / skip 5036件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1294 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $240.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.53** / 初期 $100.00 (+23.53%)
- 確定: 2956件 (Win 878 / Loss 1165 / Flat 913) / pending 0件 / skip 3270件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000320 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $123.53

## 6. Latest Market Context

- 更新: 2026-09-17T00:31:48.848933+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=76365.0
- Funnel: target 1059 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONE/USDT:USDT | +62.92% | $1,746,573.31 |
| BATON/USDT:USDT | +54.81% | $2,289,402.97 |
| HNT/USDT:USDT | +16.11% | $5,144,749.64 |
| BULLA/USDT:USDT | +10.92% | $8,803,013.78 |
| ON/USDT:USDT | +10.65% | $2,675,816.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPX/USDT:USDT | below_1h_threshold | +3.46% | +3.21% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.22% | +2.96% |
| NEAR/USDT:USDT | below_1h_threshold | +3.06% | +2.80% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.64% | +2.39% |
| ENA/USDT:USDT | below_1h_threshold | +2.28% | +2.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
