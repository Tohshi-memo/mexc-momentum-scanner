# Decision Report

- generated_at: 2026-05-25T18:29:19.097187+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4868**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=4868, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +1.74% | **+0.26%** |
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.04% | **+0.01%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.19% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/10 | 80.0% | +1.25% | **+1.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.02% | **+0.71%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.39% | **+0.56%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.73% | **+0.51%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.31** / 初期 $100.00 (+27.31%)
- 確定: 673件 (Win 169 / Loss 214 / Flat 290) / skip 756件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $127.31

## 4. Latest Market Context

- 更新: 2026-05-25T18:29:17.013392+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=77601.9
- Funnel: target 765 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +75.71% | $1,273,669.14 |
| NIL/USDT:USDT | +7.41% | $17,590,787.87 |
| H/USDT:USDT | +6.85% | $2,336,467.26 |
| GRASS/USDT:USDT | +6.79% | $3,749,524.67 |
| PHA/USDT:USDT | +6.55% | $4,090,480.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +3.24% | +3.15% |
| BEAT/USDT:USDT | below_1h_threshold | +2.13% | +2.04% |
| WLD/USDT:USDT | below_1h_threshold | +2.08% | +1.98% |
| LAB/USDT:USDT | below_1h_threshold | +1.82% | +1.72% |
| XPL/USDT:USDT | below_1h_threshold | +1.73% | +1.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
