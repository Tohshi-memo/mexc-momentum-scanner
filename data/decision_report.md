# Decision Report

- generated_at: 2026-05-20T17:15:05.062078+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4562**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4562, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.28% | **-1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.15% | **+0.46%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.19% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| ASK_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.57% | **+0.90%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.09% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.95** / 初期 $100.00 (+24.95%)
- 確定: 524件 (Win 137 / Loss 177 / Flat 210) / skip 599件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $124.95

## 4. Latest Market Context

- 更新: 2026-05-20T17:15:02.847261+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77358.4
- Funnel: target 763 → liquid 127 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +21.13% | $37,619,063.73 |
| EDEN/USDT:USDT | +17.30% | $28,553,454.32 |
| NIL/USDT:USDT | +4.18% | $1,511,061.14 |
| SATO/USDT:USDT | +3.62% | $3,184,435.09 |
| PENDLE/USDT:USDT | +3.60% | $1,782,361.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SATO/USDT:USDT | below_1h_threshold | +2.93% | +2.86% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.91% | +2.84% |
| PLAY/USDT:USDT | below_1h_threshold | +2.47% | +2.39% |
| EDEN/USDT:USDT | below_1h_threshold | +2.30% | +2.22% |
| BSB/USDT:USDT | below_1h_threshold | +2.03% | +1.96% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
