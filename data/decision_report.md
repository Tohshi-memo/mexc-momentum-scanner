# Decision Report

- generated_at: 2026-07-19T08:31:23.145647+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9013**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9013, expectancy=-0.00%
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
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.34% | **+0.23%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.99% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.23% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.32% | **+1.86%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.83% | **+1.83%** |
| MARKET_LONG | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.77% | **+0.35%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +0.73% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$394.83** / 初期 $100.00 (+294.83%)
- 確定: 3075件 (Win 962 / Loss 977 / Flat 1136) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $394.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.13** / 初期 $100.00 (+26.13%)
- 確定: 974件 (Win 248 / Loss 197 / Flat 529) / skip 1450件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2477 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $126.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.34** / 初期 $100.00 (+0.34%)
- 確定: 216件 (Win 68 / Loss 109 / Flat 39) / pending 6件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000518 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $100.34

## 6. Latest Market Context

- 更新: 2026-07-19T08:31:13.220397+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=64636.6
- Funnel: target 885 → liquid 123 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.3 >= 65=1, 4h RSI 73.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +137.08% | $43,448,227.46 |
| BANK/USDT:USDT | +61.47% | $18,492,403.96 |
| TLM/USDT:USDT | +49.77% | $5,436,597.88 |
| B/USDT:USDT | +32.01% | $39,757,456.03 |
| BULLA/USDT:USDT | +25.49% | $1,284,400.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +4.10% | +4.19% |
| BULLA/USDT:USDT | below_1h_threshold | +3.69% | +3.78% |
| TAG/USDT:USDT | below_1h_threshold | +2.90% | +2.98% |
| 1000BONK/USDT:USDT | below_1h_threshold | +2.26% | +2.35% |
| B/USDT:USDT | below_1h_threshold | +1.80% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
