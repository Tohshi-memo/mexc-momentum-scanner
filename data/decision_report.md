# Decision Report

- generated_at: 2026-11-04T18:56:45.465841+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18132**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18132, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.76% | **-1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.46% | **+0.21%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.53% | **+1.59%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.71% | **+1.48%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.39% | **+1.19%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.07% | **+1.08%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.11% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 262件 (TP 96 / SL 158 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,524.38** / 初期 $100.00 (+1424.38%)
- 確定: 6951件 (Win 2011 / Loss 2228 / Flat 2712) / skip 7742件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLANKER/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,524.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$377.23** / 初期 $100.00 (+277.23%)
- 確定: 4542件 (Win 1219 / Loss 1020 / Flat 2303) / skip 7001件
- 成長率目線: 平均log +0.000292 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLANKER/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $377.23

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6298件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000092 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-04T18:56:29.856131+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=80270.0
- Funnel: target 1078 → liquid 187 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLANKER/USDT:USDT | +25.84% | $10,932,463.73 |
| AIN/USDT:USDT | +9.18% | $2,120,412.44 |
| FLUID/USDT:USDT | +6.18% | $1,796,721.97 |
| LYN/USDT:USDT | +5.30% | $1,263,035.55 |
| BMT/USDT:USDT | +3.67% | $1,817,360.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLUID/USDT:USDT | below_1h_threshold | +4.24% | +4.38% |
| JCT/USDT:USDT | below_1h_threshold | +3.40% | +3.55% |
| INTW/USDT:USDT | below_1h_threshold | +3.24% | +3.38% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.39% | +2.54% |
| BMT/USDT:USDT | below_1h_threshold | +1.84% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
