# Decision Report

- generated_at: 2026-05-08T07:37:43.913114+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3754**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.81% / filled 20/20。**
- 全期間 MARKET基準: n=3754, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.92% | **+0.92%** |
| MARKET | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.41% | **+0.37%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +3.11% | **+0.93%** |
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |
| ASK_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.63% | **+0.22%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +0.47% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 25件 (TP 6 / SL 17 / EXP 2)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 125件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T07:37:38.461996+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=79502.1
- Funnel: target 772 → liquid 184 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +33.24% | $4,350,379.46 |
| BSB/USDT:USDT | +29.12% | $5,113,888.97 |
| SATO/USDT:USDT | +29.08% | $9,064,779.46 |
| NOT/USDT:USDT | +21.39% | $10,385,171.13 |
| LAB/USDT:USDT | +18.02% | $206,248,045.14 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +4.60% | +4.58% |
| CHZ/USDT:USDT | below_1h_threshold | +4.35% | +4.33% |
| SATO/USDT:USDT | below_1h_threshold | +2.60% | +2.58% |
| STRK/USDT:USDT | below_1h_threshold | +2.18% | +2.16% |
| MOVR/USDT:USDT | below_1h_threshold | +1.75% | +1.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
