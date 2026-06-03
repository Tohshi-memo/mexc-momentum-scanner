# Decision Report

- generated_at: 2026-06-03T13:41:22.290173+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5547**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=5547, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.04% | **+0.36%** |
| ASK | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.07% | **+1.02%** |
| MARKET_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.47% | **+0.33%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.12% | **+0.08%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$132.52** / 初期 $100.00 (+32.52%)
- 確定: 1001件 (Win 239 / Loss 310 / Flat 452) / skip 1107件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BP/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $132.52

## 4. Latest Market Context

- 更新: 2026-06-03T13:41:17.098708+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=66940.0
- Funnel: target 771 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1, 4h RSI 74.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +41.70% | $1,365,353.14 |
| CLO/USDT:USDT | +37.65% | $5,364,424.91 |
| EPIC/USDT:USDT | +32.13% | $3,160,138.24 |
| ENA/USDT:USDT | +30.97% | $64,569,106.60 |
| WLD/USDT:USDT | +30.17% | $217,368,070.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +4.19% | +4.35% |
| GUA/USDT:USDT | below_1h_threshold | +3.34% | +3.51% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.29% | +3.46% |
| GENIUS/USDT:USDT | below_1h_threshold | +3.18% | +3.35% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +3.07% | +3.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
