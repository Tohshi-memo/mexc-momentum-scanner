# Decision Report

- generated_at: 2026-07-19T01:36:13.965753+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8992**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8992, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | +2.35% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.34% | **+2.67%** |
| MARKET_LONG | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +4.04% | **+2.22%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +5.64% | **+1.98%** |
| LIMIT_5PCT_LONG | 4/20 | 20.0% | +8.00% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$371.97** / 初期 $100.00 (+271.97%)
- 確定: 3055件 (Win 950 / Loss 973 / Flat 1132) / skip 2498件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $371.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$123.13** / 初期 $100.00 (+23.13%)
- 確定: 953件 (Win 240 / Loss 192 / Flat 521) / skip 1450件
- 成長率目線: 平均log +0.000218 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2296 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $123.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.38** / 初期 $100.00 (-0.62%)
- 確定: 198件 (Win 63 / Loss 107 / Flat 28) / pending 1件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000670 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $99.38

## 6. Latest Market Context

- 更新: 2026-07-19T01:36:07.348273+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64750.2
- Funnel: target 885 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +106.03% | $32,017,481.53 |
| BANK/USDT:USDT | +47.05% | $18,805,458.95 |
| TLM/USDT:USDT | +21.97% | $2,907,592.11 |
| AKE/USDT:USDT | +19.02% | $83,913,011.87 |
| B/USDT:USDT | +17.31% | $32,808,538.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +4.87% | +4.87% |
| TRADOOR/USDT:USDT | below_1h_threshold | +3.31% | +3.32% |
| BILL/USDT:USDT | below_1h_threshold | +2.17% | +2.18% |
| BSB/USDT:USDT | below_1h_threshold | +1.50% | +1.51% |
| ANSEM/USDT:USDT | below_1h_threshold | +0.90% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
