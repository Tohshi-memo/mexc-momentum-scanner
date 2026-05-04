# Decision Report

- generated_at: 2026-05-04T08:17:22.808616+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3169**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.07% / filled 20/20。**
- 全期間 MARKET基準: n=3169, expectancy=-0.16%
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
| LIMIT_1PCT | 17/20 | 85.0% | +1.44% | **+1.23%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.62% | **+1.05%** |
| LIMIT_2PCT | 13/20 | 65.0% | +1.51% | **+0.98%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.04% | **+0.02%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.15% | **-0.08%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.58% | **-0.35%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T08:17:20.738867+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=79689.4
- Funnel: target 761 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +52.76% | $49,128,158.58 |
| BSB/USDT:USDT | +42.10% | $24,439,864.61 |
| TST/USDT:USDT | +38.84% | $6,916,420.04 |
| 4/USDT:USDT | +36.00% | $1,134,799.66 |
| TAG/USDT:USDT | +35.86% | $12,346,813.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ASTEROID/USDT:USDT | below_1h_threshold | +3.26% | +3.23% |
| 4/USDT:USDT | below_1h_threshold | +3.16% | +3.13% |
| GIGA/USDT:USDT | below_1h_threshold | +2.42% | +2.39% |
| UB/USDT:USDT | below_1h_threshold | +2.30% | +2.27% |
| ZBT/USDT:USDT | below_1h_threshold | +0.98% | +0.95% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
