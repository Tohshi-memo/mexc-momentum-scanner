# Decision Report

- generated_at: 2026-07-19T08:16:14.853926+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9012**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9012, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/17 | 17.6% | +2.08% | **+0.37%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.34% | **+0.23%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 3/20 | 15.0% | +1.00% | **+0.15%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.02% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.48% | **+2.11%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.83% | **+1.83%** |
| MARKET_LONG | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.45% | **+0.65%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +1.30% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$394.83** / 初期 $100.00 (+294.83%)
- 確定: 3074件 (Win 962 / Loss 977 / Flat 1135) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $394.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.13** / 初期 $100.00 (+26.13%)
- 確定: 973件 (Win 248 / Loss 197 / Flat 528) / skip 1450件
- 成長率目線: 平均log +0.000239 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2417 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $126.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.34** / 初期 $100.00 (+0.34%)
- 確定: 215件 (Win 68 / Loss 109 / Flat 38) / pending 4件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000548 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $100.34

## 6. Latest Market Context

- 更新: 2026-07-19T08:16:08.341819+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64664.6
- Funnel: target 885 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +137.23% | $42,691,905.75 |
| TLM/USDT:USDT | +56.26% | $5,253,450.85 |
| BANK/USDT:USDT | +45.01% | $17,753,457.25 |
| B/USDT:USDT | +31.30% | $39,574,177.98 |
| BULLA/USDT:USDT | +22.93% | $1,268,305.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.70% | +4.74% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.73% | +2.77% |
| HOME/USDT:USDT | below_1h_threshold | +2.43% | +2.47% |
| BULLA/USDT:USDT | below_1h_threshold | +1.68% | +1.72% |
| TAG/USDT:USDT | below_1h_threshold | +1.49% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
