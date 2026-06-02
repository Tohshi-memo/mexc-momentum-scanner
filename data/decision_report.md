# Decision Report

- generated_at: 2026-06-02T16:52:41.932309+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5468**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.88% / filled 20/20。**
- 全期間 MARKET基準: n=5468, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.01% | **+1.91%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.19% | **+1.02%** |
| ASK | 20/20 | 100.0% | +0.89% | **+0.89%** |
| MARKET | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_BB3S | 6/19 | 31.6% | +1.13% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.51% | **+1.13%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +1.32% | **+0.86%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.87% | **+0.48%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 88件 (TP 26 / SL 59 / EXP 3)
- 最新: STG/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1053件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T16:52:33.975446+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.55% price=67646.4
- Funnel: target 773 → liquid 153 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.0 >= 65=1, 4h RSI 91.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ENA/USDT:USDT | +10.62% | $33,044,607.68 |
| PORTAL/USDT:USDT | +8.96% | $9,933,098.01 |
| LIT/USDT:USDT | +7.22% | $2,398,773.70 |
| PIEVERSE/USDT:USDT | +6.62% | $5,251,857.47 |
| CHIP/USDT:USDT | +6.43% | $5,392,283.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZORA/USDT:USDT | below_relative_strength | +5.06% | +4.51% |
| USELESS/USDT:USDT | below_1h_threshold | +4.92% | +4.37% |
| ZEC/USDT:USDT | below_1h_threshold | +4.87% | +4.31% |
| VVV/USDT:USDT | below_1h_threshold | +4.84% | +4.28% |
| ICP/USDT:USDT | below_1h_threshold | +4.78% | +4.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
