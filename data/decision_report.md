# Decision Report

- generated_at: 2026-10-31T02:21:29.933601+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17876**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17876, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +6.27% | **+1.88%** |
| LIMIT_6PCT | 9/20 | 45.0% | +2.59% | **+1.17%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.97% | **+0.89%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.31% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.69% | **+2.15%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.39% | **+2.15%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +2.62% | **+2.10%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.13% | **+0.62%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +0.80% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,515.94** / 初期 $100.00 (+1415.94%)
- 確定: 6807件 (Win 1975 / Loss 2182 / Flat 2650) / skip 7630件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,515.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$366.27** / 初期 $100.00 (+266.27%)
- 確定: 4376件 (Win 1178 / Loss 983 / Flat 2215) / skip 6911件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0409 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $366.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6038件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-31T02:21:14.079925+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=77349.9
- Funnel: target 1090 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +31.57% | $6,454,179.82 |
| SOPH/USDT:USDT | +20.60% | $1,385,165.93 |
| IDOL/USDT:USDT | +16.83% | $14,334,768.77 |
| LSK/USDT:USDT | +11.70% | $4,826,107.48 |
| OP/USDT:USDT | +9.76% | $16,000,911.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.19% | +4.20% |
| LSK/USDT:USDT | below_1h_threshold | +1.63% | +1.65% |
| PYTH/USDT:USDT | below_1h_threshold | +1.46% | +1.47% |
| XPL/USDT:USDT | below_1h_threshold | +0.67% | +0.68% |
| MUU/USDT:USDT | below_1h_threshold | +0.65% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
