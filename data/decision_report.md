# Decision Report

- generated_at: 2026-06-14T21:58:54.751242+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6705**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=6705, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.29% | **+0.57%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.87% | **+0.75%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.17% | **+0.59%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.46% | **+0.30%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.23% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$172.74** / 初期 $100.00 (+72.74%)
- 確定: 1578件 (Win 420 / Loss 498 / Flat 660) / skip 1688件
- 成長率目線: 平均log +0.000346 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $172.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.70** / 初期 $100.00 (-1.30%)
- 確定: 75件 (Win 20 / Loss 15 / Flat 40) / skip 41件
- 成長率目線: 平均log -0.000175 / 幾何平均 -0.017% per trade / maxDD +2.07%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0481 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.70

## 5. Latest Market Context

- 更新: 2026-06-14T21:58:49.749348+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +2.11% price=65328.2
- Funnel: target 770 → liquid 135 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=41, below_relative_strength=5, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.7 >= 65=1, 4h RSI 69.6 >= 65=1, 4h RSI 67.2 >= 65=1, 4h RSI 65.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OPG/USDT:USDT | +36.03% | $2,891,023.03 |
| EVAA/USDT:USDT | +31.79% | $12,180,909.38 |
| RIF/USDT:USDT | +15.12% | $8,894,116.72 |
| EDEN/USDT:USDT | +14.89% | $1,130,935.06 |
| BP/USDT:USDT | +12.72% | $1,070,768.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGU/USDT:USDT | below_relative_strength | +5.55% | +3.44% |
| BANANAS31/USDT:USDT | below_relative_strength | +5.47% | +3.36% |
| RIVER/USDT:USDT | below_relative_strength | +5.25% | +3.14% |
| BP/USDT:USDT | below_relative_strength | +5.22% | +3.11% |
| RAVE/USDT:USDT | below_relative_strength | +5.15% | +3.04% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
