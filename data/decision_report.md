# Decision Report

- generated_at: 2026-05-05T04:27:21.643367+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3305**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3305, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.24% | **-0.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/10 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.27% | **+0.64%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.35% | **+1.28%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.53% | **+0.37%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.36% | **+0.22%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.62% | **+0.19%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.21% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定トレード: 15件 (TP 5 / SL 8 / EXP 2)
- 最新: RAVE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.85
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T04:27:19.435657+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80847.4
- Funnel: target 764 → liquid 204 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +84.66% | $6,284,902.82 |
| FHE/USDT:USDT | +26.25% | $3,343,314.42 |
| 4/USDT:USDT | +24.24% | $2,133,878.27 |
| B3/USDT:USDT | +20.03% | $1,192,587.21 |
| TONCOIN/USDT:USDT | +19.50% | $63,781,509.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FHE/USDT:USDT | below_1h_threshold | +4.66% | +4.65% |
| B3/USDT:USDT | below_1h_threshold | +4.61% | +4.59% |
| ASTEROID/USDT:USDT | below_1h_threshold | +3.06% | +3.05% |
| 4/USDT:USDT | below_1h_threshold | +2.72% | +2.70% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.56% | +2.55% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
