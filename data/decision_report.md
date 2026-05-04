# Decision Report

- generated_at: 2026-05-04T08:32:42.540423+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3170**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.07% / filled 20/20。**
- 全期間 MARKET基準: n=3170, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+2.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |
| ASK | 20/20 | 100.0% | +2.03% | **+2.03%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.38% | **+1.18%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.81% | **+1.18%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.72% | **+0.86%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.71% | **+0.42%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.15% | **-0.08%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.58% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T08:32:37.571984+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=79741.3
- Funnel: target 760 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +53.03% | $49,503,642.69 |
| BSB/USDT:USDT | +44.14% | $25,057,521.95 |
| TAG/USDT:USDT | +41.55% | $12,682,788.60 |
| TST/USDT:USDT | +36.50% | $6,962,006.72 |
| GIGA/USDT:USDT | +33.01% | $1,203,636.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.20% | +4.10% |
| UB/USDT:USDT | below_1h_threshold | +4.16% | +4.06% |
| AGT/USDT:USDT | below_1h_threshold | +3.13% | +3.03% |
| ONDO/USDT:USDT | below_1h_threshold | +2.97% | +2.87% |
| H/USDT:USDT | below_1h_threshold | +2.81% | +2.71% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
