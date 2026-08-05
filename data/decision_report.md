# Decision Report

- generated_at: 2026-08-05T04:26:33.041418+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10352**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10352, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/18 | 27.8% | +1.60% | **+0.44%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +3.11% | **+2.18%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.27% | **+1.64%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_7PCT_LONG | 3/20 | 15.0% | +4.97% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$603.82** / 初期 $100.00 (+503.82%)
- 確定: 3749件 (Win 1188 / Loss 1225 / Flat 1336) / skip 3164件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HFT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $603.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.53** / 初期 $100.00 (+40.53%)
- 確定: 1289件 (Win 361 / Loss 300 / Flat 628) / skip 2474件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0367 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.53

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.82** / 初期 $100.00 (+18.82%)
- 確定: 1108件 (Win 357 / Loss 426 / Flat 325) / pending 6件 / skip 716件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000307 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $118.82

## 6. Latest Market Context

- 更新: 2026-08-05T04:26:22.213779+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64099.2
- Funnel: target 939 → liquid 182 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.2 >= 65=1, 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +84.74% | $9,579,847.47 |
| BLESS/USDT:USDT | +35.54% | $22,327,869.97 |
| TAKE/USDT:USDT | +32.94% | $1,568,347.20 |
| CASHCAT/USDT:USDT | +31.71% | $1,180,653.18 |
| HFT/USDT:USDT | +29.67% | $1,146,592.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.98% | +5.05% |
| AKE/USDT:USDT | below_1h_threshold | +4.18% | +4.25% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.86% | +2.94% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.85% | +2.92% |
| MVLL/USDT:USDT | below_1h_threshold | +2.82% | +2.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
