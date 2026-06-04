# Decision Report

- generated_at: 2026-06-04T14:26:33.192377+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5630**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5630, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_BB3S | 2/17 | 11.8% | +3.35% | **+0.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.55% | **+0.41%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +0.69% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$98.55** / 初期 $100.00 (-1.45%)
- 確定トレード: 95件 (TP 29 / SL 63 / EXP 3)
- 最新: OPN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.55
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.20** / 初期 $100.00 (+31.20%)
- 確定: 1007件 (Win 239 / Loss 312 / Flat 456) / skip 1184件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $131.20

## 4. Latest Market Context

- 更新: 2026-06-04T14:26:30.222766+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=64071.3
- Funnel: target 772 → liquid 172 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1, 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ZEST/USDT:USDT | +78.70% | $1,566,142.33 |
| EPIC/USDT:USDT | +35.44% | $6,888,934.08 |
| HEI/USDT:USDT | +33.28% | $4,949,650.75 |
| OPN/USDT:USDT | +30.21% | $43,609,851.69 |
| SIREN/USDT:USDT | +19.48% | $9,443,569.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +4.07% | +4.27% |
| HEI/USDT:USDT | below_1h_threshold | +3.84% | +4.04% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.99% |
| WLFI/USDT:USDT | below_1h_threshold | +1.57% | +1.77% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.43% | +1.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
