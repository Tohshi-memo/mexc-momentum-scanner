# Decision Report

- generated_at: 2026-05-04T09:32:18.848437+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3176**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=3176, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 13/20 | 65.0% | +1.10% | **+0.71%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.30% | **+0.43%** |
| ASK | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.56% | **+0.37%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.15% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T09:32:16.610638+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=79677.0
- Funnel: target 761 → liquid 179 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +69.38% | $7,911,553.76 |
| SKYAI/USDT:USDT | +59.30% | $49,937,533.98 |
| TAG/USDT:USDT | +48.12% | $13,604,526.56 |
| GIGA/USDT:USDT | +39.25% | $1,264,027.15 |
| BSB/USDT:USDT | +38.68% | $25,889,641.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +4.49% | +4.48% |
| GIGGLE/USDT:USDT | below_1h_threshold | +4.39% | +4.37% |
| DASH/USDT:USDT | below_1h_threshold | +4.08% | +4.07% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.91% | +3.90% |
| ZBT/USDT:USDT | below_1h_threshold | +3.54% | +3.53% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
