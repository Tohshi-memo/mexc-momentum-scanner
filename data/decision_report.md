# Decision Report

- generated_at: 2026-09-02T03:31:24.720014+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13295**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13295, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.21% | **+0.48%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +3.54% | **+3.10%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.97% | **+1.59%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.65% | **+1.32%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 197件 (TP 73 / SL 119 / EXP 5)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$828.79** / 初期 $100.00 (+728.79%)
- 確定: 4930件 (Win 1502 / Loss 1624 / Flat 1804) / skip 4926件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $828.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.81** / 初期 $100.00 (+75.81%)
- 確定: 2274件 (Win 635 / Loss 545 / Flat 1094) / skip 4432件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0905 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $175.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2678件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T03:31:15.229911+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=77597.4
- Funnel: target 1036 → liquid 159 → pre 50 → checked 49 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=1

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +28.82% | $18,633,565.35 |
| MAGMA/USDT:USDT | +27.34% | $5,313,030.28 |
| CASHCAT/USDT:USDT | +25.39% | $1,439,321.80 |
| FILECOIN/USDT:USDT | +11.25% | $22,959,098.59 |
| ACE/USDT:USDT | +9.08% | $11,591,136.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_relative_strength | +5.26% | +4.88% |
| SKR/USDT:USDT | below_1h_threshold | +4.83% | +4.45% |
| CASHCAT/USDT:USDT | below_1h_threshold | +4.68% | +4.30% |
| PYTH/USDT:USDT | below_1h_threshold | +3.38% | +2.99% |
| CRV/USDT:USDT | below_1h_threshold | +2.69% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
