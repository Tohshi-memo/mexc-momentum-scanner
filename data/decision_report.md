# Decision Report

- generated_at: 2026-11-08T18:21:25.711135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18473**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18473, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.22% | **-1.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.21% | **+0.48%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.86% | **+2.51%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.62% | **+2.22%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.36% | **+2.02%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.65% | **+1.73%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +4.31% | **+1.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,667.41** / 初期 $100.00 (+1567.41%)
- 確定: 7151件 (Win 2057 / Loss 2280 / Flat 2814) / skip 7883件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIOT/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,667.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4756件 (Win 1277 / Loss 1047 / Flat 2432) / skip 7128件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1846 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_10PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6633件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000497 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T18:21:09.452793+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=75911.3
- Funnel: target 1089 → liquid 104 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +43.68% | $34,805,558.94 |
| AIOT/USDT:USDT | +17.73% | $4,809,259.22 |
| SOXL/USDT:USDT | +3.65% | $7,529,759.48 |
| Q/USDT:USDT | +3.39% | $2,354,616.44 |
| SNDKSTOCK/USDT:USDT | +2.40% | $3,125,428.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIOT/USDT:USDT | below_1h_threshold | +3.54% | +3.28% |
| PONS/USDT:USDT | below_1h_threshold | +3.22% | +2.96% |
| USELESS/USDT:USDT | below_1h_threshold | +2.31% | +2.05% |
| HOT/USDT:USDT | below_1h_threshold | +2.05% | +1.79% |
| Q/USDT:USDT | below_1h_threshold | +1.74% | +1.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
