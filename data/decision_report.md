# Decision Report

- generated_at: 2026-09-14T00:06:21.312449+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14470**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.07% / filled 20/20。**
- 全期間 MARKET基準: n=14470, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.76% | **+1.67%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.34% | **+1.07%** |
| MARKET | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.90% | **+3.90%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.24% | **+1.23%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.18% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,075.03** / 初期 $100.00 (+975.03%)
- 確定: 5433件 (Win 1635 / Loss 1761 / Flat 2037) / skip 5598件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,075.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.42** / 初期 $100.00 (+128.42%)
- 確定: 2988件 (Win 830 / Loss 715 / Flat 1443) / skip 4893件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0578 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: POWER/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $228.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.50** / 初期 $100.00 (+26.50%)
- 確定: 2857件 (Win 850 / Loss 1106 / Flat 901) / pending 0件 / skip 3081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POWER/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.50

## 6. Latest Market Context

- 更新: 2026-09-14T00:06:06.894023+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=76863.2
- Funnel: target 1068 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POWER/USDT:USDT | +25.91% | $3,381,613.31 |
| BTW/USDT:USDT | +10.70% | $9,887,624.25 |
| MAGMA/USDT:USDT | +6.87% | $1,782,492.43 |
| BR/USDT:USDT | +6.36% | $2,213,513.20 |
| USELESS/USDT:USDT | +3.45% | $5,417,637.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VTHO/USDT:USDT | below_1h_threshold | +2.94% | +2.87% |
| RAVE/USDT:USDT | below_1h_threshold | +1.04% | +0.97% |
| EGLD/USDT:USDT | below_1h_threshold | +0.87% | +0.80% |
| VVV/USDT:USDT | below_1h_threshold | +0.83% | +0.75% |
| FILECOIN/USDT:USDT | below_1h_threshold | +0.76% | +0.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
