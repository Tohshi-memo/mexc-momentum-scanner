# Decision Report

- generated_at: 2026-05-05T08:02:25.586953+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3331**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3331, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.72% | **-2.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/13 | 30.8% | +1.86% | **+0.57%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.04% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.92% | **+0.38%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.15% | **-0.05%** |
| LIMIT_4PCT | 17/20 | 85.0% | -0.19% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +4.22% | **+3.16%** |
| MARKET_LONG | 20/20 | 100.0% | +2.92% | **+2.92%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +4.62% | **+2.54%** |
| ASK_LONG | 20/20 | 100.0% | +2.21% | **+2.21%** |
| LIMIT_BB3S_LONG | 2/7 | 28.6% | +4.71% | **+1.35%** |

## 2. $100 Live Portfolio

- 残高: **$100.84** / 初期 $100.00 (+0.84%)
- 確定トレード: 17件 (TP 5 / SL 10 / EXP 2)
- 最新: M/USDT:USDT SL_HIT PnL -3.86% 残高後 $100.84
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-05T08:02:23.691595+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80830.1
- Funnel: target 765 → liquid 199 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +109.65% | $11,679,755.46 |
| M/USDT:USDT | +38.67% | $5,724,146.51 |
| FHE/USDT:USDT | +35.59% | $4,077,589.96 |
| HIVE/USDT:USDT | +34.27% | $3,705,320.20 |
| LAB/USDT:USDT | +30.99% | $77,870,519.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +3.44% | +3.42% |
| M/USDT:USDT | below_1h_threshold | +1.22% | +1.20% |
| LAB/USDT:USDT | below_1h_threshold | +1.17% | +1.15% |
| FHE/USDT:USDT | below_1h_threshold | +0.97% | +0.95% |
| NOT/USDT:USDT | below_1h_threshold | +0.86% | +0.85% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
