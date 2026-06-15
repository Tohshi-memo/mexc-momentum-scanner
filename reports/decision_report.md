# Decision Report

- generated_at: 2026-06-15T04:33:43.105349+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6742**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6742, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +3.14% | **+0.94%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |
| LIMIT_7PCT | 6/20 | 30.0% | +0.54% | **+0.16%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.20% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.63% | **+1.14%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.11% | **+0.72%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.02** / 初期 $100.00 (+73.02%)
- 確定: 1615件 (Win 423 / Loss 502 / Flat 690) / skip 1688件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $173.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.19** / 初期 $100.00 (+0.19%)
- 確定: 109件 (Win 24 / Loss 17 / Flat 68) / skip 44件
- 成長率目線: 平均log +0.000018 / 幾何平均 +0.002% per trade / maxDD +2.07%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0789 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $100.19

## 5. Latest Market Context

- 更新: 2026-06-15T04:26:41.932182+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=65686.0
- Funnel: target 770 → liquid 144 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.9 >= 65=1, 4h RSI 93.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +145.62% | $2,282,943.82 |
| EVAA/USDT:USDT | +73.06% | $18,925,842.06 |
| CLO/USDT:USDT | +35.07% | $2,081,684.13 |
| RIF/USDT:USDT | +34.90% | $4,992,657.96 |
| WLD/USDT:USDT | +19.89% | $103,921,283.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLD/USDT:USDT | below_1h_threshold | +3.79% | +4.11% |
| NEAR/USDT:USDT | below_1h_threshold | +2.72% | +3.03% |
| NIL/USDT:USDT | below_1h_threshold | +2.56% | +2.87% |
| JTO/USDT:USDT | below_1h_threshold | +2.22% | +2.53% |
| FET/USDT:USDT | below_1h_threshold | +1.89% | +2.20% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
