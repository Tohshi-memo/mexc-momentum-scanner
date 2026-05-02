# Decision Report

- generated_at: 2026-05-02T05:07:02.843508+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2864**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2864, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 4/17 | 23.5% | +0.92% | **+0.22%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.20% | **+1.87%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.32% | **+1.62%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| ASK_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.76% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 7件 (TP 4 / SL 3 / EXP 0)
- 最新: BIO/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T05:07:01.146129+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=78138.2
- Funnel: target 755 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +162.68% | $42,542,410.75 |
| B/USDT:USDT | +18.05% | $73,940,005.60 |
| SKYAI/USDT:USDT | +16.43% | $20,965,154.56 |
| PLAY/USDT:USDT | +12.03% | $4,504,153.35 |
| FIGHT/USDT:USDT | +7.67% | $1,032,734.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +4.54% | +4.54% |
| LAB/USDT:USDT | below_1h_threshold | +3.21% | +3.21% |
| GUA/USDT:USDT | below_1h_threshold | +2.02% | +2.02% |
| UB/USDT:USDT | below_1h_threshold | +1.53% | +1.53% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.22% | +1.22% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
