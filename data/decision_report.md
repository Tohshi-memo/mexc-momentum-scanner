# Decision Report

- generated_at: 2026-08-22T00:16:19.167316+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12278**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12278, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.51% | **-1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +5.54% | **+1.94%** |
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.19% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.59% | **+2.69%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +5.21% | **+2.34%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.55% | **+2.29%** |
| MARKET_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.78% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$682.34** / 初期 $100.00 (+582.34%)
- 確定: 4398件 (Win 1346 / Loss 1439 / Flat 1613) / skip 4441件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $682.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1884件 (Win 520 / Loss 450 / Flat 914) / skip 3805件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1676 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.64** / 初期 $100.00 (+17.64%)
- 確定: 1829件 (Win 543 / Loss 694 / Flat 592) / pending 1件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000374 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.12% 残高後 $117.64

## 6. Latest Market Context

- 更新: 2026-08-22T00:16:10.499754+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.45% price=77955.3
- Funnel: target 1018 → liquid 214 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +249.27% | $3,284,512.71 |
| CATE/USDT:USDT | +75.95% | $11,546,578.55 |
| JIMOTHY/USDT:USDT | +21.63% | $1,630,037.89 |
| AGI/USDT:USDT | +16.12% | $1,602,170.35 |
| STX/USDT:USDT | +13.92% | $2,059,781.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +4.76% | +5.21% |
| BEAT/USDT:USDT | below_1h_threshold | +3.69% | +4.14% |
| ONG/USDT:USDT | below_1h_threshold | +3.55% | +4.00% |
| PROM/USDT:USDT | below_1h_threshold | +1.98% | +2.43% |
| DASH/USDT:USDT | below_1h_threshold | +1.94% | +2.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
