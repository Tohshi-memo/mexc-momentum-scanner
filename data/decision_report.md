# Decision Report

- generated_at: 2026-06-09T16:20:08.246281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6147**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=6147, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.28% | **+1.28%** |
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.06% | **+0.96%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.23% | **+0.92%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.94% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.93% | **+0.49%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.51% | **+0.36%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.17% | **+0.12%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.14% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.75** / 初期 $100.00 (+48.75%)
- 確定: 1187件 (Win 297 / Loss 373 / Flat 517) / skip 1521件
- 成長率目線: 平均log +0.000335 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: POWER/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $148.75

## 4. Latest Market Context

- 更新: 2026-06-09T16:20:02.908270+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=60867.0
- Funnel: target 778 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SIREN/USDT:USDT | +11.50% | $8,987,434.65 |
| CHZ/USDT:USDT | +2.53% | $10,248,010.24 |
| H/USDT:USDT | +1.80% | $76,028,488.58 |
| POL/USDT:USDT | +0.80% | $1,320,388.61 |
| LAB/USDT:USDT | +0.41% | $18,556,133.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHZ/USDT:USDT | below_1h_threshold | +2.54% | +2.93% |
| H/USDT:USDT | below_1h_threshold | +1.71% | +2.10% |
| POL/USDT:USDT | below_1h_threshold | +0.71% | +1.10% |
| LAB/USDT:USDT | below_1h_threshold | +0.41% | +0.80% |
| ZBCN/USDT:USDT | below_1h_threshold | +0.30% | +0.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
