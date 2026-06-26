# Decision Report

- generated_at: 2026-06-26T00:56:37.464678+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7599**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7599, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| ASK | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.50% | **+2.38%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.56% | **+2.05%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.16% | **+1.51%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$220.62** / 初期 $100.00 (+120.62%)
- 確定: 2133件 (Win 630 / Loss 715 / Flat 788) / skip 2027件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: G/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $220.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 379件 (Win 103 / Loss 100 / Flat 176) / skip 631件
- 成長率目線: 平均log +0.000193 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARX/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T00:56:33.242229+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=59659.6
- Funnel: target 807 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.2 >= 65=1, 4h RSI 85.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| G/USDT:USDT | +29.37% | $3,037,766.00 |
| IP/USDT:USDT | +24.50% | $3,952,696.00 |
| AIN/USDT:USDT | +19.52% | $1,891,614.03 |
| IDOL/USDT:USDT | +17.26% | $1,615,829.52 |
| BAS/USDT:USDT | +14.01% | $6,241,804.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APE/USDT:USDT | below_1h_threshold | +4.73% | +4.92% |
| AIN/USDT:USDT | below_1h_threshold | +3.86% | +4.04% |
| IDOL/USDT:USDT | below_1h_threshold | +3.78% | +3.96% |
| BAS/USDT:USDT | below_1h_threshold | +3.66% | +3.85% |
| BEAT/USDT:USDT | below_1h_threshold | +3.58% | +3.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
