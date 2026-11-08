# Decision Report

- generated_at: 2026-11-08T10:46:18.443932+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18435**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18435, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 5/20 | 25.0% | +7.49% | **+1.87%** |
| LIMIT_8PCT | 7/20 | 35.0% | +5.06% | **+1.77%** |
| LIMIT_9PCT | 6/20 | 30.0% | +4.86% | **+1.46%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.34% | **+1.00%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.34% | **+0.82%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +5.64% | **+5.01%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.30% | **+1.72%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.85% | **+1.57%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.55% | **+0.77%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,641.22** / 初期 $100.00 (+1541.22%)
- 確定: 7130件 (Win 2052 / Loss 2276 / Flat 2802) / skip 7866件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $1,641.22

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4755件 (Win 1277 / Loss 1047 / Flat 2431) / skip 7091件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1217 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6597件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000432 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T10:46:05.671905+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=75864.4
- Funnel: target 1089 → liquid 104 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +280.92% | $12,317,343.66 |
| JCT/USDT:USDT | +85.54% | $5,312,781.44 |
| KOMA/USDT:USDT | +17.76% | $1,285,210.92 |
| AIOT/USDT:USDT | +13.04% | $3,022,291.47 |
| ICNT/USDT:USDT | +10.23% | $4,498,965.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +2.45% | +2.49% |
| SOXL/USDT:USDT | below_1h_threshold | +0.82% | +0.87% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.76% | +0.81% |
| IDOL/USDT:USDT | below_1h_threshold | +0.52% | +0.56% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +0.32% | +0.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
