# Decision Report

- generated_at: 2026-08-21T22:56:26.843107+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12270**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12270, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_8PCT | 5/20 | 25.0% | +8.00% | **+2.00%** |
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_BB3S | 7/19 | 36.8% | +4.24% | **+1.56%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.30% | **+1.98%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.21% | **+1.03%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.98% | **+0.93%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.25% | **+0.88%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$662.28** / 初期 $100.00 (+562.28%)
- 確定: 4390件 (Win 1343 / Loss 1439 / Flat 1608) / skip 4441件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SHIB/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $662.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.41** / 初期 $100.00 (+54.41%)
- 確定: 1877件 (Win 516 / Loss 449 / Flat 912) / skip 3804件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1094 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SHIB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T22:56:12.482172+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=78526.1
- Funnel: target 1018 → liquid 219 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.3 >= 65=1, 4h RSI 93.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +184.94% | $2,916,869.89 |
| CATE/USDT:USDT | +54.42% | $10,919,102.34 |
| JIMOTHY/USDT:USDT | +30.43% | $1,598,232.07 |
| AGI/USDT:USDT | +16.93% | $1,519,365.09 |
| SHIB/USDT:USDT | +16.61% | $40,374,659.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOKI/USDT:USDT | below_1h_threshold | +4.64% | +4.60% |
| PEPE/USDT:USDT | below_1h_threshold | +4.01% | +3.96% |
| WIF/USDT:USDT | below_1h_threshold | +3.93% | +3.88% |
| AGI/USDT:USDT | below_1h_threshold | +3.76% | +3.71% |
| PENGU/USDT:USDT | below_1h_threshold | +3.50% | +3.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
