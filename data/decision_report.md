# Decision Report

- generated_at: 2026-05-08T17:02:56.084412+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3807**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.74% / filled 20/20。**
- 全期間 MARKET基準: n=3807, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.74% | **+1.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.74% | **+1.74%** |
| ASK | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.33% | **+1.13%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.50% | **+0.33%** |
| LIMIT_5PCT | 2/20 | 10.0% | +0.95% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.03% | **+0.57%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.16% | **+0.09%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.15% | **+0.06%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.35% | **-0.07%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | -0.16% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$98.82** / 初期 $100.00 (-1.18%)
- 確定トレード: 27件 (TP 7 / SL 18 / EXP 2)
- 最新: RKLBSTOCK/USDT:USDT SL_HIT PnL -2.88% 残高後 $98.82
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 192件 (Win 48 / Loss 64 / Flat 80) / skip 176件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FILECOIN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T17:02:52.521360+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79843.6
- Funnel: target 772 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SIREN/USDT:USDT | +8.96% | $13,394,869.56 |
| INTCSTOCK/USDT:USDT | +8.65% | $6,391,816.46 |
| CHIP/USDT:USDT | +7.07% | $47,629,300.96 |
| JUP/USDT:USDT | +6.37% | $3,524,351.00 |
| ONDO/USDT:USDT | +4.85% | $73,634,428.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +4.67% | +4.58% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.93% | +1.83% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.69% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.75% | +1.65% |
| PLAY/USDT:USDT | below_1h_threshold | +0.96% | +0.86% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
