# Decision Report

- generated_at: 2026-06-06T14:00:03.473917+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5838**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.54% / filled 20/20。**
- 全期間 MARKET基準: n=5838, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.54% | **+0.54%** |
| ASK | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.31% | **+1.31%** |
| ASK_LONG | 20/20 | 100.0% | +1.07% | **+1.07%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$99.50** / 初期 $100.00 (-0.50%)
- 確定トレード: 1件 (TP 0 / SL 1 / EXP 0)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1014件 (Win 239 / Loss 313 / Flat 462) / skip 1385件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T13:59:56.753971+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=60791.6
- Funnel: target 771 → liquid 148 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.6 >= 65=1, 4h RSI 87.2 >= 65=1, 4h RSI 71.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +111.67% | $64,920,699.25 |
| BLUAI/USDT:USDT | +71.47% | $4,671,188.13 |
| HEI/USDT:USDT | +53.19% | $3,477,276.52 |
| VELVET/USDT:USDT | +49.28% | $3,597,934.76 |
| CLO/USDT:USDT | +31.04% | $2,568,120.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +2.63% | +2.97% |
| BILL/USDT:USDT | below_1h_threshold | +2.05% | +2.39% |
| VVV/USDT:USDT | below_1h_threshold | +1.91% | +2.25% |
| EPIC/USDT:USDT | below_1h_threshold | +1.41% | +1.75% |
| ENA/USDT:USDT | below_1h_threshold | +1.35% | +1.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
