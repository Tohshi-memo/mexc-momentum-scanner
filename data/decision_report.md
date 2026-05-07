# Decision Report

- generated_at: 2026-05-07T22:22:39.679499+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3713**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3713, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.16% | **+0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_ATR | 8/20 | 40.0% | +1.44% | **+0.58%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.70% | **+0.52%** |
| LIMIT_BB3S | 3/19 | 15.8% | +1.73% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.08% | **+0.65%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.53% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 23件 (TP 6 / SL 15 / EXP 2)
- 最新: D/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.32
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 85件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-07T22:22:36.674777+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=79937.4
- Funnel: target 765 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +45.06% | $7,557,855.11 |
| NIL/USDT:USDT | +44.08% | $18,341,499.50 |
| TST/USDT:USDT | +19.42% | $5,825,835.35 |
| DYDX/USDT:USDT | +18.65% | $9,735,554.86 |
| LAB/USDT:USDT | +18.55% | $225,119,716.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +2.96% | +2.64% |
| LIGHT/USDT:USDT | below_1h_threshold | +2.87% | +2.56% |
| D/USDT:USDT | below_1h_threshold | +2.25% | +1.93% |
| EVAA/USDT:USDT | below_1h_threshold | +1.84% | +1.52% |
| HIGH/USDT:USDT | below_1h_threshold | +1.80% | +1.48% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
