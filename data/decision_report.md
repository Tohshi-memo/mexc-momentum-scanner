# Decision Report

- generated_at: 2026-05-04T08:47:21.833880+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3172**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.08% / filled 20/20。**
- 全期間 MARKET基準: n=3172, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+2.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.08% | **+2.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.08% | **+2.08%** |
| ASK | 20/20 | 100.0% | +2.03% | **+2.03%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.72% | **+0.86%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.54% | **+0.85%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.98% | **+0.78%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.82% | **+0.49%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.17% | **-0.08%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.60% | **-0.36%** |

## 2. $100 Live Portfolio

- 残高: **$103.40** / 初期 $100.00 (+3.40%)
- 確定トレード: 12件 (TP 5 / SL 5 / EXP 2)
- 最新: B2/USDT:USDT EXPIRED PnL +1.44% 残高後 $103.40
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T08:47:16.936471+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=79680.0
- Funnel: target 760 → liquid 178 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.6 >= 65=1, 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +50.82% | $49,979,440.68 |
| TAG/USDT:USDT | +47.56% | $12,980,685.16 |
| BSB/USDT:USDT | +42.96% | $25,498,429.27 |
| TST/USDT:USDT | +41.83% | $7,070,642.49 |
| ASTEROID/USDT:USDT | +30.51% | $3,533,513.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.30% | +4.28% |
| LAB/USDT:USDT | below_1h_threshold | +3.81% | +3.79% |
| TST/USDT:USDT | below_1h_threshold | +3.71% | +3.69% |
| AGT/USDT:USDT | below_1h_threshold | +3.12% | +3.10% |
| BR/USDT:USDT | below_1h_threshold | +2.88% | +2.86% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
