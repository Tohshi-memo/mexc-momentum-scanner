# Decision Report

- generated_at: 2026-05-05T08:12:20.568805+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3334**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3334, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-3.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -3.39% | **-3.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.47% | **+0.44%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.47% | **+0.24%** |
| LIMIT_BB3S | 2/12 | 16.7% | +1.29% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +4.49% | **+3.82%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +5.75% | **+3.45%** |
| MARKET_LONG | 20/20 | 100.0% | +3.19% | **+3.19%** |
| ASK_LONG | 20/20 | 100.0% | +2.58% | **+2.58%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +5.95% | **+2.08%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T08:12:18.082687+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80830.0
- Funnel: target 765 → liquid 199 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +105.31% | $12,242,563.27 |
| LAB/USDT:USDT | +47.05% | $79,758,448.33 |
| HIVE/USDT:USDT | +36.56% | $3,760,003.85 |
| FHE/USDT:USDT | +36.05% | $4,191,328.53 |
| M/USDT:USDT | +35.92% | $6,007,684.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.78% | +1.76% |
| NOT/USDT:USDT | below_1h_threshold | +1.71% | +1.69% |
| DOGS/USDT:USDT | below_1h_threshold | +1.58% | +1.57% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.56% | +1.55% |
| HIVE/USDT:USDT | below_1h_threshold | +1.40% | +1.39% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
