# Decision Report

- generated_at: 2026-09-23T09:31:19.716435+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15424**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.49% / filled 20/20。**
- 全期間 MARKET基準: n=15424, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +3.03% | **+2.12%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.98% | **+2.09%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.18% | **+1.64%** |
| LIMIT_BB3S | 5/11 | 45.5% | +3.37% | **+1.53%** |
| MARKET | 20/20 | 100.0% | +1.49% | **+1.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.06% | **+0.90%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.89% | **+0.67%** |
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +0.87% | **+0.61%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.51% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5895件 (Win 1739 / Loss 1890 / Flat 2266) / skip 6090件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.37** / 初期 $100.00 (+147.37%)
- 確定: 3373件 (Win 930 / Loss 789 / Flat 1654) / skip 5462件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0190 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $247.37

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.73** / 初期 $100.00 (+21.73%)
- 確定: 3135件 (Win 923 / Loss 1233 / Flat 979) / pending 1件 / skip 3761件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000197 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZAMA/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.73

## 6. Latest Market Context

- 更新: 2026-09-23T09:31:09.214175+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=85896.9
- Funnel: target 1061 → liquid 191 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAKE/USDT:USDT | +226.45% | $4,011,287.45 |
| SHROOM/USDT:USDT | +64.88% | $1,347,709.96 |
| MET/USDT:USDT | +31.61% | $1,184,724.85 |
| ALLO/USDT:USDT | +26.56% | $3,236,408.10 |
| SUPER/USDT:USDT | +26.22% | $1,024,133.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +4.81% | +4.79% |
| MET/USDT:USDT | below_1h_threshold | +4.65% | +4.62% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.50% | +3.47% |
| GRASS/USDT:USDT | below_1h_threshold | +3.42% | +3.39% |
| BLESS/USDT:USDT | below_1h_threshold | +2.90% | +2.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
