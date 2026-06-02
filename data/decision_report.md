# Decision Report

- generated_at: 2026-06-02T16:36:59.377346+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5466**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=5466, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.85% | **+0.81%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| ASK | 20/20 | 100.0% | +0.29% | **+0.29%** |
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.91% | **+1.33%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.68% | **+1.01%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.20% | **+0.14%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 88件 (TP 26 / SL 59 / EXP 3)
- 最新: STG/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.05** / 初期 $100.00 (+31.05%)
- 確定: 975件 (Win 229 / Loss 299 / Flat 447) / skip 1052件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +7.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MRVLSTOCK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.05

## 4. Latest Market Context

- 更新: 2026-06-02T16:36:56.048850+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.59% price=67669.3
- Funnel: target 773 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=2, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.5 >= 65=1, 4h RSI 65.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +6.39% | $4,865,277.53 |
| CHIP/USDT:USDT | +5.70% | $5,120,471.48 |
| ENA/USDT:USDT | +5.48% | $29,200,600.21 |
| ICP/USDT:USDT | +5.14% | $12,635,217.13 |
| LIT/USDT:USDT | +4.95% | $2,305,587.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ENA/USDT:USDT | below_relative_strength | +5.55% | +4.97% |
| ICP/USDT:USDT | below_relative_strength | +5.18% | +4.59% |
| LIT/USDT:USDT | below_1h_threshold | +4.96% | +4.38% |
| APE/USDT:USDT | below_1h_threshold | +4.55% | +3.96% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.19% | +3.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
