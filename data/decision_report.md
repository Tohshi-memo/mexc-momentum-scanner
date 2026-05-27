# Decision Report

- generated_at: 2026-05-27T14:04:33.842874+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4927**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.61% / filled 20/20。**
- 全期間 MARKET基準: n=4927, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.61% | **+1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.70% | **+1.70%** |
| MARKET | 20/20 | 100.0% | +1.61% | **+1.61%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.45% | **+1.30%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.81% | **+0.57%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.57% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.56% | **+0.37%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | -0.35% | **-0.19%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | -0.29% | **-0.27%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -1.56% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.79** / 初期 $100.00 (+26.79%)
- 確定: 684件 (Win 172 / Loss 220 / Flat 292) / skip 804件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $126.79

## 4. Latest Market Context

- 更新: 2026-05-27T14:04:31.722498+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=75172.2
- Funnel: target 775 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +17.57% | $1,612,958.58 |
| BEAT/USDT:USDT | +16.92% | $23,425,052.15 |
| FF/USDT:USDT | +12.31% | $1,236,792.32 |
| LUNC/USDT:USDT | +12.12% | $15,626,943.94 |
| MYX/USDT:USDT | +9.81% | $1,479,723.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FILECOIN/USDT:USDT | below_1h_threshold | +1.12% | +0.96% |
| MYX/USDT:USDT | below_1h_threshold | +1.04% | +0.88% |
| XLM/USDT:USDT | below_1h_threshold | +0.96% | +0.81% |
| RDDTSTOCK/USDT:USDT | below_1h_threshold | +0.89% | +0.74% |
| UB/USDT:USDT | below_1h_threshold | +0.75% | +0.59% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
