# Decision Report

- generated_at: 2026-08-02T12:21:18.185530+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10159**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.88% / filled 20/20。**
- 全期間 MARKET基準: n=10159, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.88% | **+1.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.65% | **+1.48%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.41% | **+1.02%** |
| LIMIT_BB3S | 2/19 | 10.5% | +6.00% | **+0.63%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.36% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | -0.00% | **-0.00%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | -0.43% | **-0.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$566.31** / 初期 $100.00 (+466.31%)
- 確定: 3674件 (Win 1166 / Loss 1205 / Flat 1303) / skip 3046件
- 成長率目線: 平均log +0.000472 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $566.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1281件 (Win 359 / Loss 298 / Flat 624) / skip 2289件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0076 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.52** / 初期 $100.00 (+12.52%)
- 確定: 965件 (Win 306 / Loss 377 / Flat 282) / pending 4件 / skip 662件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GIGGLE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $112.52

## 6. Latest Market Context

- 更新: 2026-08-02T12:21:10.939638+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=63159.0
- Funnel: target 922 → liquid 132 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +59.86% | $18,359,331.95 |
| HOME/USDT:USDT | +31.05% | $4,361,182.79 |
| UAI/USDT:USDT | +26.35% | $26,844,477.39 |
| HYPER/USDT:USDT | +16.91% | $1,655,329.51 |
| 1000RATS/USDT:USDT | +14.89% | $34,425,519.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +2.18% | +1.93% |
| PENGU/USDT:USDT | below_1h_threshold | +1.37% | +1.13% |
| GIGGLE/USDT:USDT | below_1h_threshold | +0.87% | +0.62% |
| ZEN/USDT:USDT | below_1h_threshold | +0.78% | +0.54% |
| HEI/USDT:USDT | below_1h_threshold | +0.72% | +0.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
