# Decision Report

- generated_at: 2026-05-02T17:11:59.027637+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2963**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=2963, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.25% | **+1.19%** |
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |
| ASK | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.41% | **+0.34%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.54% | **+0.46%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.32% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T17:11:57.203302+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78399.6
- Funnel: target 755 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAG/USDT:USDT | +23.93% | $13,806,356.45 |
| TAC/USDT:USDT | +12.02% | $2,530,324.33 |
| LAB/USDT:USDT | +11.96% | $202,132,735.06 |
| XNY/USDT:USDT | +8.17% | $1,235,142.81 |
| PNUT/USDT:USDT | +6.23% | $1,398,256.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +2.27% | +2.29% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.94% | +1.97% |
| H/USDT:USDT | below_1h_threshold | +1.88% | +1.91% |
| LYN/USDT:USDT | below_1h_threshold | +1.19% | +1.22% |
| TAC/USDT:USDT | below_1h_threshold | +0.97% | +0.99% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
