# Decision Report

- generated_at: 2026-06-02T16:47:14.266819+00:00
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

- 更新: 2026-06-02T16:47:07.429369+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.75% price=67779.3
- Funnel: target 773 → liquid 153 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=43, below_relative_strength=3, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.8 >= 65=1, 4h RSI 91.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ENA/USDT:USDT | +11.35% | $32,192,984.89 |
| CHIP/USDT:USDT | +6.89% | $5,298,213.85 |
| LIT/USDT:USDT | +6.78% | $2,347,353.31 |
| PIEVERSE/USDT:USDT | +6.41% | $5,207,629.85 |
| PORTAL/USDT:USDT | +5.69% | $9,887,900.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_relative_strength | +5.70% | +4.95% |
| ICP/USDT:USDT | below_relative_strength | +5.35% | +4.60% |
| USELESS/USDT:USDT | below_relative_strength | +5.12% | +4.37% |
| ZORA/USDT:USDT | below_1h_threshold | +4.80% | +4.05% |
| ZEC/USDT:USDT | below_1h_threshold | +4.36% | +3.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
