# Decision Report

- generated_at: 2026-11-15T04:11:23.235690+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18929**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.57% / filled 20/20。**
- 全期間 MARKET基準: n=18929, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.57% | **+1.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.76% | **+0.65%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.61% | **+0.46%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.01% | **+0.45%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +2.10% | **+0.63%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.57% | **+0.43%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.65% | **+0.42%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.44% | **+0.33%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.31% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,720.31** / 初期 $100.00 (+1620.31%)
- 確定: 7333件 (Win 2106 / Loss 2347 / Flat 2880) / skip 8157件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,720.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$428.00** / 初期 $100.00 (+328.00%)
- 確定: 4937件 (Win 1320 / Loss 1080 / Flat 2537) / skip 7403件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0351 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $428.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7090件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000208 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-15T04:11:12.120216+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=64674.5
- Funnel: target 1071 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SHELL/USDT:USDT | +12.99% | $2,332,866.48 |
| VVV/USDT:USDT | +10.30% | $2,331,645.69 |
| PIEVERSE/USDT:USDT | +9.05% | $1,616,631.10 |
| ARIA/USDT:USDT | +7.52% | $2,392,005.79 |
| INIT/USDT:USDT | +3.72% | $1,856,126.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +2.51% | +2.70% |
| GPS/USDT:USDT | below_1h_threshold | +1.84% | +2.03% |
| H/USDT:USDT | below_1h_threshold | +1.27% | +1.46% |
| SHELL/USDT:USDT | below_1h_threshold | +1.24% | +1.43% |
| DODO/USDT:USDT | below_1h_threshold | +0.81% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
