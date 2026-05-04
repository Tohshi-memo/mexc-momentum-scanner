# Decision Report

- generated_at: 2026-05-04T08:37:30.029065+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3171**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.67% / filled 20/20。**
- 全期間 MARKET基準: n=3171, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+2.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.67% | **+2.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.67% | **+2.67%** |
| ASK | 20/20 | 100.0% | +2.63% | **+2.63%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.66% | **+1.33%** |
| LIMIT_ATR | 12/20 | 60.0% | +2.07% | **+1.24%** |
| LIMIT_BB3S | 4/13 | 30.8% | +3.69% | **+1.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.64% | **+0.42%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.24% | **-0.13%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | -0.70% | **-0.46%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T08:37:25.557654+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=79661.2
- Funnel: target 760 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +52.93% | $49,637,893.31 |
| BSB/USDT:USDT | +43.68% | $25,244,348.63 |
| TAG/USDT:USDT | +42.16% | $12,736,275.16 |
| TST/USDT:USDT | +33.66% | $7,023,115.80 |
| GIGA/USDT:USDT | +33.07% | $1,205,663.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +4.94% | +4.94% |
| LAB/USDT:USDT | below_1h_threshold | +4.35% | +4.35% |
| H/USDT:USDT | below_1h_threshold | +3.11% | +3.11% |
| GIGA/USDT:USDT | below_1h_threshold | +2.42% | +2.43% |
| ZEN/USDT:USDT | below_1h_threshold | +2.37% | +2.37% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
