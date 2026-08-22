# Decision Report

- generated_at: 2026-08-22T02:16:15.978221+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12294**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12294, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.11% | **-1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.55% | **+0.54%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.12% | **+0.28%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.39% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.52% | **+2.82%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.90% | **+1.74%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.85% | **+1.66%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.45% | **+1.22%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$694.25** / 初期 $100.00 (+594.25%)
- 確定: 4412件 (Win 1351 / Loss 1442 / Flat 1619) / skip 4443件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $694.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.47** / 初期 $100.00 (+54.47%)
- 確定: 1900件 (Win 523 / Loss 455 / Flat 922) / skip 3805件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2321 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.98** / 初期 $100.00 (+17.98%)
- 確定: 1843件 (Win 546 / Loss 696 / Flat 601) / pending 2件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000515 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.98

## 6. Latest Market Context

- 更新: 2026-08-22T02:16:07.138604+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=78105.1
- Funnel: target 1018 → liquid 217 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +279.38% | $3,874,860.22 |
| CATE/USDT:USDT | +58.70% | $11,984,702.77 |
| AGI/USDT:USDT | +31.07% | $1,748,595.02 |
| ZEC/USDT:USDT | +24.94% | $311,472,210.90 |
| ZEN/USDT:USDT | +19.97% | $3,121,601.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRB/USDT:USDT | below_1h_threshold | +4.89% | +4.51% |
| ZEN/USDT:USDT | below_1h_threshold | +4.35% | +3.97% |
| GALA/USDT:USDT | below_1h_threshold | +3.96% | +3.58% |
| ORDI/USDT:USDT | below_1h_threshold | +3.44% | +3.05% |
| AGI/USDT:USDT | below_1h_threshold | +2.86% | +2.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
