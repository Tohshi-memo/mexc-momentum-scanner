# Decision Report

- generated_at: 2026-07-19T04:26:13.184342+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8997**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8997, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.56% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.53% | **+2.27%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.04% | **+2.13%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.84% | **+0.92%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$366.89** / 初期 $100.00 (+266.89%)
- 確定: 3060件 (Win 951 / Loss 977 / Flat 1132) / skip 2498件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $366.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$122.05** / 初期 $100.00 (+22.05%)
- 確定: 958件 (Win 241 / Loss 196 / Flat 521) / skip 1450件
- 成長率目線: 平均log +0.000208 / 幾何平均 +0.021% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2095 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $122.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.30** / 初期 $100.00 (-0.70%)
- 確定: 201件 (Win 64 / Loss 109 / Flat 28) / pending 3件 / skip 264件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000592 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.30

## 6. Latest Market Context

- 更新: 2026-07-19T04:26:06.563507+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64652.4
- Funnel: target 885 → liquid 121 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +122.61% | $37,042,656.24 |
| BANK/USDT:USDT | +39.14% | $18,687,142.09 |
| B/USDT:USDT | +25.79% | $35,415,926.95 |
| TLM/USDT:USDT | +16.38% | $3,214,974.73 |
| ANSEM/USDT:USDT | +9.41% | $1,888,538.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +4.47% | +4.53% |
| VELVET/USDT:USDT | below_1h_threshold | +3.59% | +3.65% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.75% | +2.80% |
| B/USDT:USDT | below_1h_threshold | +2.53% | +2.59% |
| TAG/USDT:USDT | below_1h_threshold | +1.58% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
