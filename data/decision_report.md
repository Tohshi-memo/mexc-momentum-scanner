# Decision Report

- generated_at: 2026-07-18T10:41:25.929792+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8934**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8934, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.97% | **+0.59%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.02% | **+0.51%** |
| LIMIT_BB3S | 3/16 | 18.8% | +0.73% | **+0.14%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.65% | **+0.10%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.01% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.68% | **+1.09%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.40% | **+0.60%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.95% | **+0.59%** |
| MARKET_LONG | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$358.77** / 初期 $100.00 (+258.77%)
- 確定: 3049件 (Win 946 / Loss 973 / Flat 1130) / skip 2446件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $358.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.89** / 初期 $100.00 (+10.89%)
- 確定: 895件 (Win 214 / Loss 181 / Flat 500) / skip 1450件
- 成長率目線: 平均log +0.000115 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0454 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $110.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.42** / 初期 $100.00 (-0.58%)
- 確定: 189件 (Win 60 / Loss 102 / Flat 27) / pending 6件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000253 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.42

## 6. Latest Market Context

- 更新: 2026-07-18T10:41:19.730346+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63975.3
- Funnel: target 885 → liquid 166 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.0 >= 65=1, 4h RSI 81.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +41.43% | $69,362,541.46 |
| B/USDT:USDT | +33.13% | $4,261,886.77 |
| TRADOOR/USDT:USDT | +31.73% | $4,452,566.01 |
| ALLO/USDT:USDT | +13.65% | $4,386,211.99 |
| ROAM/USDT:USDT | +13.24% | $1,031,039.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +4.66% | +4.63% |
| BANK/USDT:USDT | below_1h_threshold | +2.41% | +2.39% |
| ALLO/USDT:USDT | below_1h_threshold | +2.23% | +2.21% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.57% | +1.54% |
| LAB/USDT:USDT | below_1h_threshold | +1.44% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
