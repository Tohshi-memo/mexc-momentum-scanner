# Decision Report

- generated_at: 2026-05-29T05:44:51.277463+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5012**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5012, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.04% | **+0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.45% | **+0.34%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.65% | **+0.39%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.76% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 734件 (Win 175 / Loss 222 / Flat 337) / skip 839件
- 成長率目線: 平均log +0.000339 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-29T05:44:44.082461+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=73493.3
- Funnel: target 777 → liquid 149 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.7 >= 65=1, 4h RSI 95.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +94.75% | $38,128,687.29 |
| CTR/USDT:USDT | +39.47% | $1,190,617.54 |
| DELLSTOCK/USDT:USDT | +36.38% | $8,159,950.25 |
| CLO/USDT:USDT | +27.57% | $1,576,907.71 |
| LAB/USDT:USDT | +19.37% | $43,011,234.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +4.08% | +4.04% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.61% | +3.58% |
| XLM/USDT:USDT | below_1h_threshold | +2.91% | +2.87% |
| DYDX/USDT:USDT | below_1h_threshold | +2.62% | +2.59% |
| INJ/USDT:USDT | below_1h_threshold | +2.45% | +2.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
