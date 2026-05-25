# Decision Report

- generated_at: 2026-05-25T22:09:11.183064+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4872**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.39% / filled 20/20。**
- 全期間 MARKET基準: n=4872, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.88% | **+1.88%** |
| MARKET | 20/20 | 100.0% | +1.39% | **+1.39%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.21% | **+1.03%** |
| LIMIT_BB3S | 6/11 | 54.5% | +0.77% | **+0.42%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.30% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +1.72% | **+1.03%** |
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +0.82% | **+0.73%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.84% | **+0.71%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.60% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.31** / 初期 $100.00 (+27.31%)
- 確定: 673件 (Win 169 / Loss 214 / Flat 290) / skip 760件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $127.31

## 4. Latest Market Context

- 更新: 2026-05-25T22:09:09.075784+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=77332.9
- Funnel: target 765 → liquid 120 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +74.28% | $1,595,955.15 |
| GRASS/USDT:USDT | +17.19% | $6,479,165.90 |
| WLD/USDT:USDT | +9.85% | $42,839,343.12 |
| ERA/USDT:USDT | +6.84% | $1,810,775.57 |
| AKT/USDT:USDT | +6.45% | $1,306,573.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +0.70% | +0.71% |
| LAB/USDT:USDT | below_1h_threshold | +0.56% | +0.57% |
| ERA/USDT:USDT | below_1h_threshold | +0.46% | +0.47% |
| LIT/USDT:USDT | below_1h_threshold | +0.40% | +0.41% |
| NIL/USDT:USDT | below_1h_threshold | +0.38% | +0.39% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
