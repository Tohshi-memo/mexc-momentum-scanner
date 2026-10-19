# Decision Report

- generated_at: 2026-10-19T05:56:32.654468+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16990**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16990, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.46% | **+1.21%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.74% | **+2.74%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.44% | **+2.44%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.21% | **+1.77%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.66% | **+1.73%** |

## 2. $100 Live Portfolio

- 残高: **$121.48** / 初期 $100.00 (+21.48%)
- 確定トレード: 246件 (TP 91 / SL 148 / EXP 7)
- 最新: ZEREBRO/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.48
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,290.61** / 初期 $100.00 (+1190.61%)
- 確定: 6435件 (Win 1870 / Loss 2054 / Flat 2511) / skip 7116件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $1,290.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.49** / 初期 $100.00 (+176.49%)
- 確定: 3755件 (Win 1036 / Loss 882 / Flat 1837) / skip 6646件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0120 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $276.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5154件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000113 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-19T05:56:17.402616+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=82698.8
- Funnel: target 1085 → liquid 148 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1, 4h RSI 69.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +68.67% | $13,293,112.57 |
| AGT/USDT:USDT | +29.12% | $7,465,206.19 |
| ZEREBRO/USDT:USDT | +27.27% | $1,611,109.41 |
| KORU/USDT:USDT | +17.72% | $58,397,881.64 |
| AVA/USDT:USDT | +15.29% | $2,594,044.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| APR/USDT:USDT | below_1h_threshold | +4.96% | +5.02% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +2.89% | +2.95% |
| BR/USDT:USDT | below_1h_threshold | +2.53% | +2.59% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +0.69% | +0.75% |
| SKINNOVSTOCK/USDT:USDT | below_1h_threshold | +0.68% | +0.74% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
