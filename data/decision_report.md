# Decision Report

- generated_at: 2026-05-06T07:45:55.789522+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3430**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.72% / filled 20/20。**
- 全期間 MARKET基準: n=3430, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=+1.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.77% | **+1.77%** |
| MARKET | 20/20 | 100.0% | +1.72% | **+1.72%** |
| LIMIT_BB3S | 4/10 | 40.0% | +2.40% | **+0.96%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.97% | **+0.63%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_BB3S_LONG | 8/10 | 80.0% | -0.26% | **-0.21%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.58% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-06T07:45:53.219054+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=81381.2
- Funnel: target 765 → liquid 196 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1, 4h RSI 92.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IO/USDT:USDT | +54.76% | $5,464,731.18 |
| ZEC/USDT:USDT | +37.49% | $690,151,272.45 |
| B3/USDT:USDT | +29.72% | $1,442,108.72 |
| STORJ/USDT:USDT | +27.53% | $2,452,249.73 |
| FHE/USDT:USDT | +23.33% | $28,688,323.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEN/USDT:USDT | below_1h_threshold | +4.80% | +4.87% |
| FHE/USDT:USDT | below_1h_threshold | +4.49% | +4.55% |
| DASH/USDT:USDT | below_1h_threshold | +3.57% | +3.64% |
| B3/USDT:USDT | below_1h_threshold | +3.07% | +3.13% |
| STRK/USDT:USDT | below_1h_threshold | +2.72% | +2.78% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
