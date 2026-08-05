# Decision Report

- generated_at: 2026-08-05T05:16:15.772494+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10365**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=10365, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +2.97% | **+2.54%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.89% | **+1.70%** |
| MARKET_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.24% | **+0.87%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.23% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$607.71** / 初期 $100.00 (+507.71%)
- 確定: 3760件 (Win 1192 / Loss 1230 / Flat 1338) / skip 3166件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $607.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.22** / 初期 $100.00 (+42.22%)
- 確定: 1299件 (Win 365 / Loss 303 / Flat 631) / skip 2477件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1160 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $142.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.60** / 初期 $100.00 (+18.60%)
- 確定: 1115件 (Win 359 / Loss 430 / Flat 326) / pending 4件 / skip 719件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000371 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.60

## 6. Latest Market Context

- 更新: 2026-08-05T05:16:08.281267+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=64271.5
- Funnel: target 939 → liquid 183 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +95.56% | $10,663,165.72 |
| HFT/USDT:USDT | +48.35% | $1,237,472.89 |
| BLESS/USDT:USDT | +43.14% | $23,403,582.47 |
| CASHCAT/USDT:USDT | +40.26% | $1,202,530.88 |
| TAKE/USDT:USDT | +34.24% | $1,588,047.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HFT/USDT:USDT | below_1h_threshold | +4.21% | +4.01% |
| BICO/USDT:USDT | below_1h_threshold | +4.11% | +3.90% |
| CASHCAT/USDT:USDT | below_1h_threshold | +3.65% | +3.45% |
| HEI/USDT:USDT | below_1h_threshold | +3.26% | +3.06% |
| BLESS/USDT:USDT | below_1h_threshold | +2.56% | +2.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
