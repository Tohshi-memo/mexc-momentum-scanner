# Decision Report

- generated_at: 2026-05-04T02:12:14.745706+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3126**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3126, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_BB3S | 6/20 | 30.0% | +0.72% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.47% | **+1.74%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.83% | **+1.28%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.36% | **+0.88%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T02:12:12.866580+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=79884.6
- Funnel: target 757 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +75.51% | $237,280,714.15 |
| SKYAI/USDT:USDT | +55.15% | $34,674,206.45 |
| TAG/USDT:USDT | +32.78% | $4,032,678.43 |
| BSB/USDT:USDT | +22.10% | $14,829,728.97 |
| AIGENSYN/USDT:USDT | +22.07% | $6,069,584.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.17% | +4.00% |
| TAG/USDT:USDT | below_1h_threshold | +3.14% | +2.97% |
| LAB/USDT:USDT | below_1h_threshold | +2.91% | +2.74% |
| MONAD/USDT:USDT | below_1h_threshold | +1.85% | +1.68% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.81% | +1.64% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
