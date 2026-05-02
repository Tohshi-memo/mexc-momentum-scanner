# Decision Report

- generated_at: 2026-05-02T22:12:02.985312+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2997**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2997, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +2.47% | **+0.62%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 4/18 | 22.2% | +2.65% | **+0.59%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.81% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.49% | **+0.97%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.49% | **+0.74%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| MARKET_LONG | 20/20 | 100.0% | +0.47% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 10件 (TP 5 / SL 4 / EXP 1)
- 最新: AIOT/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T22:12:01.134900+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78707.1
- Funnel: target 755 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +18.73% | $319,643,589.95 |
| FHE/USDT:USDT | +16.06% | $1,126,292.56 |
| BIANRENSHENG/USDT:USDT | +15.53% | $1,118,817.50 |
| XNY/USDT:USDT | +14.20% | $2,069,934.26 |
| NAORIS/USDT:USDT | +10.12% | $4,377,635.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.14% | +2.12% |
| PYTH/USDT:USDT | below_1h_threshold | +1.62% | +1.60% |
| BLEND/USDT:USDT | below_1h_threshold | +1.45% | +1.42% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.35% | +1.33% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.19% | +1.17% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
