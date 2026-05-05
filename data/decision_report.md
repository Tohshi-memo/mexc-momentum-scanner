# Decision Report

- generated_at: 2026-05-05T14:33:26.993456+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3360**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.67% / filled 20/20。**
- 全期間 MARKET基準: n=3360, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+2.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.67% | **+2.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.69% | **+2.69%** |
| MARKET | 20/20 | 100.0% | +2.67% | **+2.67%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.50% | **+2.37%** |
| LIMIT_ATR | 12/20 | 60.0% | +2.03% | **+1.22%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.40% | **+0.98%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | -1.45% | **-0.29%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.80% | **-0.40%** |
| MARKET_LONG | 20/20 | 100.0% | -0.49% | **-0.49%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | -1.90% | **-0.76%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T14:33:25.009994+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=81431.8
- Funnel: target 765 → liquid 192 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +76.49% | $26,004,703.85 |
| LAB/USDT:USDT | +40.46% | $103,843,030.43 |
| FHE/USDT:USDT | +34.61% | $5,810,676.95 |
| HIVE/USDT:USDT | +32.27% | $8,477,345.62 |
| TONCOIN/USDT:USDT | +25.14% | $117,089,073.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RAVE/USDT:USDT | below_1h_threshold | +4.81% | +4.62% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.55% | +4.36% |
| LUNC/USDT:USDT | below_1h_threshold | +4.38% | +4.19% |
| MORPHO/USDT:USDT | below_1h_threshold | +2.24% | +2.05% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.09% | +1.90% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
