# Decision Report

- generated_at: 2026-06-12T07:11:20.619202+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6478**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6478, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/20 | 15.0% | +3.20% | **+0.48%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.03% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.00% | **+3.00%** |
| ASK_LONG | 20/20 | 100.0% | +2.93% | **+2.93%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.32% | **+2.33%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.53% | **+1.94%** |
| LIMIT_ATR_LONG | 5/20 | 25.0% | +4.69% | **+1.17%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.79** / 初期 $100.00 (+64.79%)
- 確定: 1353件 (Win 365 / Loss 432 / Flat 556) / skip 1686件
- 成長率目線: 平均log +0.000369 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $164.79

## 4. Latest Market Context

- 更新: 2026-06-12T07:11:17.431144+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=63052.5
- Funnel: target 779 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +102.48% | $138,001,997.94 |
| ESPORTS/USDT:USDT | +55.48% | $33,811,043.83 |
| NAORIS/USDT:USDT | +36.78% | $2,116,085.99 |
| XPL/USDT:USDT | +32.28% | $7,234,595.81 |
| STG/USDT:USDT | +29.80% | $14,473,653.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +3.35% | +3.20% |
| VELVET/USDT:USDT | below_1h_threshold | +2.83% | +2.68% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.77% | +2.61% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.69% | +2.54% |
| NEAR/USDT:USDT | below_1h_threshold | +2.10% | +1.95% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
