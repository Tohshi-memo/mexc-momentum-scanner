# Decision Report

- generated_at: 2026-05-02T01:41:59.111125+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2850**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.20% / filled 20/20。**
- 全期間 MARKET基準: n=2850, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +3.63% | **+1.27%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.73% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.33% | **+0.86%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.92% | **+0.77%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.99% | **+0.74%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.84% | **+0.55%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T01:41:57.440754+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78285.9
- Funnel: target 755 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +73.80% | $25,979,933.67 |
| SKYAI/USDT:USDT | +14.19% | $21,612,784.74 |
| BLESS/USDT:USDT | +11.50% | $1,370,420.45 |
| CHILLGUY/USDT:USDT | +10.77% | $1,049,184.41 |
| FIGHT/USDT:USDT | +9.59% | $1,286,560.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.77% | +4.79% |
| ORCA/USDT:USDT | below_1h_threshold | +3.06% | +3.09% |
| RAVE/USDT:USDT | below_1h_threshold | +2.62% | +2.64% |
| TRB/USDT:USDT | below_1h_threshold | +2.44% | +2.46% |
| PLAY/USDT:USDT | below_1h_threshold | +2.21% | +2.23% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
