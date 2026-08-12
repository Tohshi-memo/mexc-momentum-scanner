# Decision Report

- generated_at: 2026-08-12T08:36:32.709470+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11346**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11346, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.15% | **-0.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.44% | **+1.37%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.25% | **+0.50%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3940件 (Win 1230 / Loss 1285 / Flat 1425) / skip 3967件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$148.29** / 初期 $100.00 (+48.29%)
- 確定: 1582件 (Win 444 / Loss 366 / Flat 772) / skip 3175件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1022 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $148.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.87** / 初期 $100.00 (+13.87%)
- 確定: 1361件 (Win 409 / Loss 531 / Flat 421) / pending 4件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000083 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $113.87

## 6. Latest Market Context

- 更新: 2026-08-12T08:36:20.786217+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63766.9
- Funnel: target 967 → liquid 186 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.2 >= 65=1, 4h RSI 68.3 >= 65=1, 4h RSI 65.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +74.82% | $2,200,170.39 |
| JIMOTHY/USDT:USDT | +62.27% | $2,447,906.25 |
| PROM/USDT:USDT | +40.26% | $7,214,256.00 |
| BEAT/USDT:USDT | +36.61% | $91,199,578.03 |
| STORJ/USDT:USDT | +23.39% | $1,021,201.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.04% | +4.10% |
| CAP/USDT:USDT | below_1h_threshold | +3.30% | +3.36% |
| NIL/USDT:USDT | below_1h_threshold | +3.23% | +3.29% |
| FHE/USDT:USDT | below_1h_threshold | +2.15% | +2.20% |
| SNXX/USDT:USDT | below_1h_threshold | +0.96% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
