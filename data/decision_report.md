# Decision Report

- generated_at: 2026-05-01T23:37:21.365996+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2843**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2843, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.36% | **+0.61%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.30% | **+0.30%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +2.89% | **+1.30%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.95% | **+1.17%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +3.58% | **+1.08%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.95% | **+0.97%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.83% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T23:37:19.404004+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=78026.5
- Funnel: target 755 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +51.52% | $14,567,143.10 |
| CHILLGUY/USDT:USDT | +12.34% | $1,096,845.86 |
| WOJAK/USDT:USDT | +10.50% | $1,072,648.38 |
| FIGHT/USDT:USDT | +8.63% | $1,263,393.81 |
| SNDKSTOCK/USDT:USDT | +7.12% | $5,760,488.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +3.06% | +3.16% |
| BSB/USDT:USDT | below_1h_threshold | +2.51% | +2.62% |
| TAG/USDT:USDT | below_1h_threshold | +1.98% | +2.09% |
| B/USDT:USDT | below_1h_threshold | +1.90% | +2.01% |
| MEGA/USDT:USDT | below_1h_threshold | +1.14% | +1.24% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
