# Decision Report

- generated_at: 2026-08-05T07:56:24.434836+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10378**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10378, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.29% | **+0.22%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.02% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +2.28% | **+2.00%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.68% | **+1.18%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.99% | **+0.90%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.89% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.48** / 初期 $100.00 (+514.48%)
- 確定: 3766件 (Win 1195 / Loss 1233 / Flat 1338) / skip 3173件
- 成長率目線: 平均log +0.000482 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HFT/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $614.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.15** / 初期 $100.00 (+44.15%)
- 確定: 1311件 (Win 370 / Loss 307 / Flat 634) / skip 2478件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1183 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $144.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.59** / 初期 $100.00 (+18.59%)
- 確定: 1125件 (Win 361 / Loss 434 / Flat 330) / pending 6件 / skip 721件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000395 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.59

## 6. Latest Market Context

- 更新: 2026-08-05T07:56:14.559551+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=64029.1
- Funnel: target 939 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HFT/USDT:USDT | +74.12% | $2,095,208.55 |
| BLESS/USDT:USDT | +64.39% | $29,015,586.45 |
| HEI/USDT:USDT | +44.22% | $16,846,789.04 |
| BICO/USDT:USDT | +35.44% | $17,359,261.26 |
| CASHCAT/USDT:USDT | +32.71% | $1,142,784.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HFT/USDT:USDT | below_1h_threshold | +4.68% | +4.99% |
| AKE/USDT:USDT | below_1h_threshold | +3.93% | +4.24% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.86% | +4.16% |
| BLESS/USDT:USDT | below_1h_threshold | +3.81% | +4.12% |
| CYS/USDT:USDT | below_1h_threshold | +3.66% | +3.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
