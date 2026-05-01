# Decision Report

- generated_at: 2026-05-01T22:12:01.812677+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2837**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=2837, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.94% | **+0.94%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.81% | **+0.77%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.48% | **+1.03%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.10% | **+0.60%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.96% | **+0.57%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.68% | **+0.51%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.91% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T22:12:00.083234+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=78249.1
- Funnel: target 755 → liquid 185 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +27.36% | $8,419,593.95 |
| RLS/USDT:USDT | +11.06% | $2,386,642.06 |
| BLESS/USDT:USDT | +7.88% | $1,065,768.70 |
| SNDKSTOCK/USDT:USDT | +7.45% | $6,090,322.59 |
| ZEC/USDT:USDT | +7.25% | $269,642,805.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +1.27% | +1.16% |
| PHAROS/USDT:USDT | below_1h_threshold | +1.18% | +1.07% |
| PLAY/USDT:USDT | below_1h_threshold | +0.90% | +0.79% |
| BRETT/USDT:USDT | below_1h_threshold | +0.88% | +0.77% |
| MOVR/USDT:USDT | below_1h_threshold | +0.78% | +0.67% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
