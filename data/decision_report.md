# Decision Report

- generated_at: 2026-06-03T02:57:45.630453+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5510**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.35% / filled 20/20。**
- 全期間 MARKET基準: n=5510, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.42% | **+1.42%** |
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.80% | **+0.54%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.57% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.02% | **+0.02%** |
| MARKET_LONG | 20/20 | 100.0% | -0.00% | **-0.00%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -1.21% | **-0.18%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 977件 (Win 229 / Loss 300 / Flat 448) / skip 1094件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-03T02:57:41.860805+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=66605.8
- Funnel: target 773 → liquid 153 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.8 >= 65=1, 4h RSI 77.1 >= 65=1, 4h RSI 79.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +35.86% | $13,906,335.66 |
| APR/USDT:USDT | +27.53% | $1,091,350.95 |
| GENIUS/USDT:USDT | +23.62% | $1,383,499.74 |
| LIT/USDT:USDT | +18.20% | $7,196,790.62 |
| BBSTOCK/USDT:USDT | +16.91% | $1,868,739.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZORA/USDT:USDT | below_1h_threshold | +2.78% | +3.21% |
| EPIC/USDT:USDT | below_1h_threshold | +2.17% | +2.60% |
| BILL/USDT:USDT | below_1h_threshold | +2.02% | +2.45% |
| BBSTOCK/USDT:USDT | below_1h_threshold | +1.67% | +2.10% |
| RENDER/USDT:USDT | below_1h_threshold | +1.64% | +2.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
