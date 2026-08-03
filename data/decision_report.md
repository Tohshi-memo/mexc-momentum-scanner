# Decision Report

- generated_at: 2026-08-03T15:56:40.636199+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10231**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10231, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.08% | **+0.04%** |
| LIMIT_9PCT | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_8PCT | 4/20 | 20.0% | -0.15% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.19% | **+2.19%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.35% | **+2.11%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.04% | **+1.82%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.94% | **+0.77%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$579.59** / 初期 $100.00 (+479.59%)
- 確定: 3690件 (Win 1170 / Loss 1207 / Flat 1313) / skip 3102件
- 成長率目線: 平均log +0.000476 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $579.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.31** / 初期 $100.00 (+40.31%)
- 確定: 1283件 (Win 359 / Loss 298 / Flat 626) / skip 2359件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0106 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.88** / 初期 $100.00 (+15.88%)
- 確定: 1014件 (Win 326 / Loss 393 / Flat 295) / pending 5件 / skip 685件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000489 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $115.88

## 6. Latest Market Context

- 更新: 2026-08-03T15:56:28.888516+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.39% price=63676.4
- Funnel: target 929 → liquid 163 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.2 >= 65=1, 4h RSI 68.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +246.83% | $4,716,923.46 |
| BICO/USDT:USDT | +49.33% | $19,137,572.93 |
| SKYAI/USDT:USDT | +31.99% | $7,623,554.43 |
| 1000RATS/USDT:USDT | +28.43% | $38,853,900.06 |
| BTW/USDT:USDT | +27.18% | $6,575,550.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.74% | +5.14% |
| TAKE/USDT:USDT | below_1h_threshold | +4.13% | +4.52% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +4.01% | +4.41% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.38% | +3.78% |
| ADA/USDT:USDT | below_1h_threshold | +2.90% | +3.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
