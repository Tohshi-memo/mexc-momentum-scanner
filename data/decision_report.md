# Decision Report

- generated_at: 2026-07-16T00:26:11.675834+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8777**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.02% / filled 20/20。**
- 全期間 MARKET基準: n=8777, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.02% | **+2.02%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.97% | **+1.87%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.55% | **+1.31%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.47% | **+0.88%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.85% | **+0.25%** |
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -2.71% | **-0.54%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 99件 (TP 34 / SL 63 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$340.65** / 初期 $100.00 (+240.65%)
- 確定: 2894件 (Win 906 / Loss 942 / Flat 1046) / skip 2444件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $340.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.10** / 初期 $100.00 (+7.10%)
- 確定: 741件 (Win 170 / Loss 168 / Flat 403) / skip 1447件
- 成長率目線: 平均log +0.000093 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1141 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.10

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 184件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000422 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-16T00:26:05.376902+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=64615.3
- Funnel: target 871 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOME/USDT:USDT | +23.43% | $1,886,659.44 |
| ROAM/USDT:USDT | +17.28% | $5,606,381.26 |
| CAP/USDT:USDT | +15.59% | $1,682,597.85 |
| ONDO/USDT:USDT | +10.26% | $41,133,881.42 |
| SKL/USDT:USDT | +8.80% | $1,851,287.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +2.44% | +2.60% |
| T/USDT:USDT | below_1h_threshold | +2.17% | +2.34% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.55% | +1.72% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.53% | +1.70% |
| CAP/USDT:USDT | below_1h_threshold | +1.42% | +1.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
